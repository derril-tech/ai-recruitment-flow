"""
Configuration settings for the Recruitment Flow AI API.

This module contains all configuration settings, environment variables,
and application constants.
"""

import os
from typing import List, Optional
from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application
    APP_NAME: str = "Recruitment Flow AI API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 1
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:3001"]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/recruitment_flow"
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 30
    DATABASE_POOL_TIMEOUT: int = 30
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_POOL_SIZE: int = 10
    
    # AI Services
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    
    # Vector Database
    VECTOR_DB_URL: str = "postgresql+asyncpg://user:password@localhost/recruitment_flow"
    
    # File Storage
    STORAGE_BUCKET: str = "recruitment-flow-storage"
    STORAGE_REGION: str = "us-east-1"
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    
    # Email
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    SMTP_USE_TLS: bool = True
    
    # Calendar Integrations
    GOOGLE_CLIENT_ID: Optional[str] = None
    GOOGLE_CLIENT_SECRET: Optional[str] = None
    MICROSOFT_CLIENT_ID: Optional[str] = None
    MICROSOFT_CLIENT_SECRET: Optional[str] = None
    
    # ATS Integrations
    GREENHOUSE_API_KEY: Optional[str] = None
    LEVER_API_KEY: Optional[str] = None
    WORKDAY_CLIENT_ID: Optional[str] = None
    WORKDAY_CLIENT_SECRET: Optional[str] = None
    
    # Monitoring
    SENTRY_DSN: Optional[str] = None
    LOG_LEVEL: str = "INFO"
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 100
    RATE_LIMIT_PER_HOUR: int = 1000
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    
    # File Upload
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_FILE_TYPES: List[str] = [
        "application/pdf",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain",
        "image/jpeg",
        "image/png"
    ]
    
    # AI Configuration
    AI_MODEL_NAME: str = "gpt-4"
    AI_MAX_TOKENS: int = 4000
    AI_TEMPERATURE: float = 0.1
    AI_SCREENING_CONFIDENCE_THRESHOLD: float = 0.7
    
    # Compliance
    DATA_RETENTION_DAYS: int = 2555  # 7 years
    GDPR_ENABLED: bool = True
    EEO_REPORTING_ENABLED: bool = True
    
    @validator("ALLOWED_ORIGINS", pre=True)
    def parse_allowed_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    @validator("ALLOWED_HOSTS", pre=True)
    def parse_allowed_hosts(cls, v):
        if isinstance(v, str):
            return [host.strip() for host in v.split(",")]
        return v
    
    @validator("ALLOWED_FILE_TYPES", pre=True)
    def parse_allowed_file_types(cls, v):
        if isinstance(v, str):
            return [file_type.strip() for file_type in v.split(",")]
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()


# Development settings override
if settings.ENVIRONMENT == "development":
    settings.DEBUG = True
    settings.LOG_LEVEL = "DEBUG"
    
    # Development defaults
    if not settings.SECRET_KEY or settings.SECRET_KEY == "your-secret-key-here":
        settings.SECRET_KEY = "dev-secret-key-change-in-production"
    
    if not settings.DATABASE_URL or "localhost" not in settings.DATABASE_URL:
        settings.DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/recruitment_flow_dev"
    
    if not settings.REDIS_URL or "localhost" not in settings.REDIS_URL:
        settings.REDIS_URL = "redis://localhost:6379/0"


# Production settings validation
if settings.ENVIRONMENT == "production":
    required_vars = [
        "SECRET_KEY",
        "DATABASE_URL",
        "REDIS_URL",
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
    ]
    
    missing_vars = [var for var in required_vars if not getattr(settings, var)]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")


# Constants
API_V1_STR = "/api/v1"
PROJECT_NAME = "Recruitment Flow AI"
PROJECT_DESCRIPTION = "Intelligent Hiring Orchestration Platform"

# Database table names
TABLES = {
    "users": "users",
    "organizations": "organizations",
    "roles": "roles",
    "candidates": "candidates",
    "profiles": "profiles",
    "screens": "screens",
    "interviews": "interviews",
    "schedules": "schedules",
    "offers": "offers",
    "audits": "audits",
    "reports": "reports",
}

# User roles and permissions
ROLES = {
    "admin": {
        "name": "Administrator",
        "permissions": ["*"]
    },
    "recruiter": {
        "name": "Recruiter",
        "permissions": [
            "read:roles",
            "write:roles",
            "read:candidates",
            "write:candidates",
            "read:interviews",
            "write:interviews",
            "read:offers",
            "write:offers",
            "read:analytics",
        ]
    },
    "hiring_manager": {
        "name": "Hiring Manager",
        "permissions": [
            "read:roles",
            "read:candidates",
            "read:interviews",
            "write:interviews",
            "read:offers",
            "write:offers",
            "read:analytics",
        ]
    },
    "interviewer": {
        "name": "Interviewer",
        "permissions": [
            "read:candidates",
            "read:interviews",
            "write:interviews",
        ]
    },
    "analyst": {
        "name": "Analyst",
        "permissions": [
            "read:roles",
            "read:candidates",
            "read:interviews",
            "read:offers",
            "read:analytics",
            "read:compliance",
        ]
    },
}

# Candidate statuses
CANDIDATE_STATUSES = [
    "applied",
    "screening",
    "interviewing",
    "offered",
    "hired",
    "rejected",
    "withdrawn",
]

# Interview types
INTERVIEW_TYPES = [
    "phone_screen",
    "technical",
    "behavioral",
    "cultural",
    "final",
    "reference",
]

# Offer statuses
OFFER_STATUSES = [
    "draft",
    "sent",
    "accepted",
    "declined",
    "expired",
    "withdrawn",
]

# Screening scores
SCREENING_SCORES = {
    "excellent": {"min": 90, "max": 100, "label": "Excellent"},
    "good": {"min": 80, "max": 89, "label": "Good"},
    "fair": {"min": 70, "max": 79, "label": "Fair"},
    "poor": {"min": 0, "max": 69, "label": "Poor"},
}

# Time zones
SUPPORTED_TIMEZONES = [
    "UTC",
    "America/New_York",
    "America/Chicago",
    "America/Denver",
    "America/Los_Angeles",
    "Europe/London",
    "Europe/Paris",
    "Asia/Tokyo",
    "Asia/Shanghai",
    "Australia/Sydney",
]
