"""
Main FastAPI application for Recruitment Flow AI.

This module contains the main FastAPI application instance and configuration
for the recruitment platform backend.
"""

import logging
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from recruitment_flow_api.core.config import settings
from recruitment_flow_api.core.logging import setup_logging
from recruitment_flow_api.api.v1.api import api_router
from recruitment_flow_api.core.database import init_db, close_db
from recruitment_flow_api.core.redis import init_redis, close_redis

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.
    
    Handles startup and shutdown events for the FastAPI application.
    """
    # Startup
    logger.info("Starting Recruitment Flow AI API...")
    
    # Initialize database connection
    await init_db()
    logger.info("Database connection initialized")
    
    # Initialize Redis connection
    await init_redis()
    logger.info("Redis connection initialized")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Recruitment Flow AI API...")
    
    # Close Redis connection
    await close_redis()
    logger.info("Redis connection closed")
    
    # Close database connection
    await close_db()
    logger.info("Database connection closed")


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title="Recruitment Flow AI API",
        description=(
            "Intelligent Hiring Orchestration Platform API. "
            "Source. Screen. Schedule. Decide—fairly and fast."
        ),
        version="1.0.0",
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
        openapi_url="/openapi.json" if settings.DEBUG else None,
        lifespan=lifespan,
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Add trusted host middleware for security
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS,
    )
    
    # Include API router
    app.include_router(api_router, prefix="/api/v1")
    
    # Add exception handlers
    app.add_exception_handler(
        StarletteHTTPException,
        http_exception_handler,
    )
    app.add_exception_handler(
        RequestValidationError,
        validation_exception_handler,
    )
    
    return app


async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException,
) -> JSONResponse:
    """
    Handle HTTP exceptions.
    
    Args:
        request: The incoming request
        exc: The HTTP exception
        
    Returns:
        JSONResponse: Error response
    """
    logger.error(
        f"HTTP Exception: {exc.status_code} - {exc.detail}",
        extra={"request": request, "exception": exc},
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "type": "http_exception",
                "message": exc.detail,
                "status_code": exc.status_code,
            }
        },
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """
    Handle validation exceptions.
    
    Args:
        request: The incoming request
        exc: The validation exception
        
    Returns:
        JSONResponse: Error response
    """
    logger.error(
        f"Validation Error: {exc.errors()}",
        extra={"request": request, "exception": exc},
    )
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "type": "validation_error",
                "message": "Request validation failed",
                "details": exc.errors(),
            }
        },
    )


# Create the application instance
app = create_application()


@app.get("/health")
async def health_check() -> Dict[str, Any]:
    """
    Health check endpoint.
    
    Returns:
        Dict containing health status and version information
    """
    return {
        "status": "healthy",
        "version": "1.0.0",
        "service": "recruitment-flow-api",
        "environment": settings.ENVIRONMENT,
    }


@app.get("/")
async def root() -> Dict[str, str]:
    """
    Root endpoint.
    
    Returns:
        Dict containing welcome message
    """
    return {
        "message": "Welcome to Recruitment Flow AI API",
        "version": "1.0.0",
        "docs": "/docs" if settings.DEBUG else "Documentation disabled in production",
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "recruitment_flow_api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info",
    )
