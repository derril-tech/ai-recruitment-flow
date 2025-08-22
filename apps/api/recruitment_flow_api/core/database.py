"""
Database configuration and connection management.

This module handles database connections, session management,
and provides utilities for database operations.
"""

import asyncio
from typing import AsyncGenerator, Optional
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
    AsyncEngine,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool

from recruitment_flow_api.core.config import settings

# Create declarative base for models
Base = declarative_base()

# Global engine and session factory
engine: Optional[AsyncEngine] = None
AsyncSessionLocal: Optional[async_sessionmaker[AsyncSession]] = None


async def init_db() -> None:
    """
    Initialize database connection and session factory.
    
    Creates the async engine and session factory for database operations.
    """
    global engine, AsyncSessionLocal
    
    if engine is not None:
        return
    
    # Create async engine
    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=settings.DEBUG,
        pool_size=settings.DATABASE_POOL_SIZE,
        max_overflow=settings.DATABASE_MAX_OVERFLOW,
        pool_timeout=settings.DATABASE_POOL_TIMEOUT,
        pool_pre_ping=True,
        pool_recycle=3600,
    )
    
    # Create session factory
    AsyncSessionLocal = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )


async def close_db() -> None:
    """
    Close database connections.
    
    Properly closes the engine and cleans up resources.
    """
    global engine, AsyncSessionLocal
    
    if engine is not None:
        await engine.dispose()
        engine = None
        AsyncSessionLocal = None


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Get database session.
    
    Yields:
        AsyncSession: Database session for dependency injection
    """
    if AsyncSessionLocal is None:
        await init_db()
    
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Get database session as context manager.
    
    Yields:
        AsyncSession: Database session
    """
    if AsyncSessionLocal is None:
        await init_db()
    
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def create_tables() -> None:
    """
    Create all database tables.
    
    Creates all tables defined in the models.
    """
    if engine is None:
        await init_db()
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables() -> None:
    """
    Drop all database tables.
    
    Drops all tables defined in the models.
    """
    if engine is None:
        await init_db()
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def check_db_connection() -> bool:
    """
    Check database connection health.
    
    Returns:
        bool: True if connection is healthy, False otherwise
    """
    try:
        if engine is None:
            await init_db()
        
        async with engine.begin() as conn:
            await conn.execute("SELECT 1")
        return True
    except Exception:
        return False


async def get_db_stats() -> dict:
    """
    Get database statistics.
    
    Returns:
        dict: Database statistics including connection pool info
    """
    if engine is None:
        return {"status": "not_initialized"}
    
    try:
        pool = engine.pool
        return {
            "status": "healthy",
            "pool_size": pool.size(),
            "checked_in": pool.checkedin(),
            "checked_out": pool.checkedout(),
            "overflow": pool.overflow(),
            "invalid": pool.invalid(),
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
        }


# Database utilities
class DatabaseManager:
    """
    Database manager for common operations.
    
    Provides utilities for common database operations
    and transaction management.
    """
    
    def __init__(self):
        self.session: Optional[AsyncSession] = None
    
    async def __aenter__(self):
        """Enter async context manager."""
        if AsyncSessionLocal is None:
            await init_db()
        
        self.session = AsyncSessionLocal()
        return self.session
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit async context manager."""
        if self.session:
            if exc_type is not None:
                await self.session.rollback()
            else:
                await self.session.commit()
            await self.session.close()


async def execute_in_transaction(func, *args, **kwargs):
    """
    Execute function within a database transaction.
    
    Args:
        func: Function to execute
        *args: Function arguments
        **kwargs: Function keyword arguments
        
    Returns:
        Result of the function execution
    """
    async with get_db_session() as session:
        try:
            result = await func(session, *args, **kwargs)
            await session.commit()
            return result
        except Exception:
            await session.rollback()
            raise


async def execute_with_retry(func, max_retries: int = 3, *args, **kwargs):
    """
    Execute function with retry logic for database operations.
    
    Args:
        func: Function to execute
        max_retries: Maximum number of retry attempts
        *args: Function arguments
        **kwargs: Function keyword arguments
        
    Returns:
        Result of the function execution
    """
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            last_exception = e
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
            continue
    
    raise last_exception
