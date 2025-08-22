"""
Redis configuration and connection management.

This module handles Redis connections, caching utilities,
and provides Redis-based services for the application.
"""

import json
import pickle
from typing import Any, Optional, Union
from contextlib import asynccontextmanager

import aioredis
from aioredis import Redis, ConnectionPool

from recruitment_flow_api.core.config import settings

# Global Redis client
redis_client: Optional[Redis] = None


async def init_redis() -> None:
    """
    Initialize Redis connection.
    
    Creates the Redis client and connection pool.
    """
    global redis_client
    
    if redis_client is not None:
        return
    
    # Create connection pool
    pool = ConnectionPool.from_url(
        settings.REDIS_URL,
        max_connections=settings.REDIS_POOL_SIZE,
        decode_responses=True,
    )
    
    # Create Redis client
    redis_client = Redis(connection_pool=pool)


async def close_redis() -> None:
    """
    Close Redis connections.
    
    Properly closes the Redis client and connection pool.
    """
    global redis_client
    
    if redis_client is not None:
        await redis_client.close()
        redis_client = None


async def get_redis() -> Redis:
    """
    Get Redis client instance.
    
    Returns:
        Redis: Redis client instance
    """
    if redis_client is None:
        await init_redis()
    
    return redis_client


async def check_redis_connection() -> bool:
    """
    Check Redis connection health.
    
    Returns:
        bool: True if connection is healthy, False otherwise
    """
    try:
        redis = await get_redis()
        await redis.ping()
        return True
    except Exception:
        return False


async def get_redis_stats() -> dict:
    """
    Get Redis statistics.
    
    Returns:
        dict: Redis statistics and info
    """
    try:
        redis = await get_redis()
        info = await redis.info()
        return {
            "status": "healthy",
            "connected_clients": info.get("connected_clients", 0),
            "used_memory_human": info.get("used_memory_human", "0B"),
            "total_commands_processed": info.get("total_commands_processed", 0),
            "keyspace_hits": info.get("keyspace_hits", 0),
            "keyspace_misses": info.get("keyspace_misses", 0),
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
        }


# Cache utilities
class CacheManager:
    """
    Cache manager for Redis-based caching operations.
    
    Provides utilities for caching data with different
    serialization formats and expiration policies.
    """
    
    def __init__(self, default_ttl: int = 3600):
        self.default_ttl = default_ttl
    
    async def get(self, key: str, default: Any = None) -> Any:
        """
        Get value from cache.
        
        Args:
            key: Cache key
            default: Default value if key not found
            
        Returns:
            Cached value or default
        """
        redis = await get_redis()
        value = await redis.get(key)
        
        if value is None:
            return default
        
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    
    async def set(
        self,
        key: str,
        value: Any,
        ttl: Optional[int] = None,
        serialize: bool = True,
    ) -> bool:
        """
        Set value in cache.
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time to live in seconds
            serialize: Whether to serialize the value
            
        Returns:
            True if successful
        """
        redis = await get_redis()
        
        if serialize:
            value = json.dumps(value)
        
        ttl = ttl or self.default_ttl
        return await redis.setex(key, ttl, value)
    
    async def delete(self, key: str) -> bool:
        """
        Delete key from cache.
        
        Args:
            key: Cache key to delete
            
        Returns:
            True if key was deleted
        """
        redis = await get_redis()
        return bool(await redis.delete(key))
    
    async def exists(self, key: str) -> bool:
        """
        Check if key exists in cache.
        
        Args:
            key: Cache key to check
            
        Returns:
            True if key exists
        """
        redis = await get_redis()
        return bool(await redis.exists(key))
    
    async def expire(self, key: str, ttl: int) -> bool:
        """
        Set expiration for key.
        
        Args:
            key: Cache key
            ttl: Time to live in seconds
            
        Returns:
            True if expiration was set
        """
        redis = await get_redis()
        return bool(await redis.expire(key, ttl))
    
    async def ttl(self, key: str) -> int:
        """
        Get time to live for key.
        
        Args:
            key: Cache key
            
        Returns:
            TTL in seconds, -1 if no expiration, -2 if key doesn't exist
        """
        redis = await get_redis()
        return await redis.ttl(key)
    
    async def clear_pattern(self, pattern: str) -> int:
        """
        Clear keys matching pattern.
        
        Args:
            pattern: Redis pattern to match
            
        Returns:
            Number of keys deleted
        """
        redis = await get_redis()
        keys = await redis.keys(pattern)
        
        if keys:
            return await redis.delete(*keys)
        return 0


# Rate limiting utilities
class RateLimiter:
    """
    Rate limiter using Redis.
    
    Provides rate limiting functionality using Redis
    with sliding window algorithm.
    """
    
    def __init__(self, redis_key_prefix: str = "rate_limit"):
        self.redis_key_prefix = redis_key_prefix
    
    async def is_allowed(
        self,
        identifier: str,
        max_requests: int,
        window_seconds: int,
    ) -> bool:
        """
        Check if request is allowed within rate limit.
        
        Args:
            identifier: Unique identifier (e.g., IP, user ID)
            max_requests: Maximum requests allowed in window
            window_seconds: Time window in seconds
            
        Returns:
            True if request is allowed
        """
        redis = await get_redis()
        key = f"{self.redis_key_prefix}:{identifier}"
        
        # Get current count
        current = await redis.get(key)
        current_count = int(current) if current else 0
        
        if current_count >= max_requests:
            return False
        
        # Increment counter
        pipe = redis.pipeline()
        pipe.incr(key)
        pipe.expire(key, window_seconds)
        await pipe.execute()
        
        return True
    
    async def get_remaining(
        self,
        identifier: str,
        max_requests: int,
    ) -> int:
        """
        Get remaining requests for identifier.
        
        Args:
            identifier: Unique identifier
            max_requests: Maximum requests allowed
            
        Returns:
            Number of remaining requests
        """
        redis = await get_redis()
        key = f"{self.redis_key_prefix}:{identifier}"
        
        current = await redis.get(key)
        current_count = int(current) if current else 0
        
        return max(0, max_requests - current_count)


# Session management utilities
class SessionManager:
    """
    Session manager using Redis.
    
    Provides session storage and management using Redis.
    """
    
    def __init__(self, session_ttl: int = 3600):
        self.session_ttl = session_ttl
    
    async def create_session(
        self,
        session_id: str,
        data: dict,
        ttl: Optional[int] = None,
    ) -> bool:
        """
        Create new session.
        
        Args:
            session_id: Unique session identifier
            data: Session data
            ttl: Time to live in seconds
            
        Returns:
            True if session was created
        """
        redis = await get_redis()
        key = f"session:{session_id}"
        ttl = ttl or self.session_ttl
        
        return await redis.setex(key, ttl, json.dumps(data))
    
    async def get_session(self, session_id: str) -> Optional[dict]:
        """
        Get session data.
        
        Args:
            session_id: Session identifier
            
        Returns:
            Session data or None if not found
        """
        redis = await get_redis()
        key = f"session:{session_id}"
        
        data = await redis.get(key)
        if data:
            return json.loads(data)
        return None
    
    async def update_session(
        self,
        session_id: str,
        data: dict,
        ttl: Optional[int] = None,
    ) -> bool:
        """
        Update session data.
        
        Args:
            session_id: Session identifier
            data: New session data
            ttl: Time to live in seconds
            
        Returns:
            True if session was updated
        """
        redis = await get_redis()
        key = f"session:{session_id}"
        ttl = ttl or self.session_ttl
        
        return await redis.setex(key, ttl, json.dumps(data))
    
    async def delete_session(self, session_id: str) -> bool:
        """
        Delete session.
        
        Args:
            session_id: Session identifier
            
        Returns:
            True if session was deleted
        """
        redis = await get_redis()
        key = f"session:{session_id}"
        
        return bool(await redis.delete(key))
    
    async def extend_session(
        self,
        session_id: str,
        ttl: Optional[int] = None,
    ) -> bool:
        """
        Extend session expiration.
        
        Args:
            session_id: Session identifier
            ttl: New time to live in seconds
            
        Returns:
            True if session was extended
        """
        redis = await get_redis()
        key = f"session:{session_id}"
        ttl = ttl or self.session_ttl
        
        return bool(await redis.expire(key, ttl))


# Global instances
cache_manager = CacheManager()
rate_limiter = RateLimiter()
session_manager = SessionManager()
