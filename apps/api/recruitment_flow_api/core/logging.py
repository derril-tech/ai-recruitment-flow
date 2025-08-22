"""
Logging configuration for the Recruitment Flow AI API.

This module sets up structured logging with different levels
and handlers for development and production environments.
"""

import logging
import sys
from typing import Dict, Any
from pathlib import Path

from recruitment_flow_api.core.config import settings


def setup_logging() -> None:
    """
    Configure logging for the application.
    
    Sets up structured logging with appropriate handlers
    and formatters based on the environment.
    """
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper()))
    
    # Clear existing handlers
    root_logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, settings.LOG_LEVEL.upper()))
    
    if settings.ENVIRONMENT == "development":
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    else:
        console_formatter = logging.Formatter(
            '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}'
        )
    
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    # File handler for production
    if settings.ENVIRONMENT == "production":
        file_handler = logging.FileHandler(log_dir / "app.log")
        file_handler.setLevel(logging.INFO)
        
        file_formatter = logging.Formatter(
            '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}'
        )
        file_handler.setFormatter(file_formatter)
        root_logger.addHandler(file_handler)
        
        # Error file handler
        error_handler = logging.FileHandler(log_dir / "error.log")
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(file_formatter)
        root_logger.addHandler(error_handler)
    
    # Set specific logger levels
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("anthropic").setLevel(logging.WARNING)
    
    # Create application logger
    logger = logging.getLogger("recruitment_flow_api")
    logger.info(f"Logging configured for {settings.ENVIRONMENT} environment")


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the specified name.
    
    Args:
        name: The name of the logger
        
    Returns:
        Logger instance
    """
    return logging.getLogger(f"recruitment_flow_api.{name}")


class StructuredLogger:
    """
    Structured logger for consistent log formatting.
    
    Provides methods for logging with structured data
    and consistent formatting across the application.
    """
    
    def __init__(self, name: str):
        self.logger = get_logger(name)
    
    def info(self, message: str, **kwargs: Any) -> None:
        """Log info message with structured data."""
        self.logger.info(message, extra=kwargs)
    
    def warning(self, message: str, **kwargs: Any) -> None:
        """Log warning message with structured data."""
        self.logger.warning(message, extra=kwargs)
    
    def error(self, message: str, **kwargs: Any) -> None:
        """Log error message with structured data."""
        self.logger.error(message, extra=kwargs)
    
    def debug(self, message: str, **kwargs: Any) -> None:
        """Log debug message with structured data."""
        self.logger.debug(message, extra=kwargs)
    
    def critical(self, message: str, **kwargs: Any) -> None:
        """Log critical message with structured data."""
        self.logger.critical(message, extra=kwargs)
    
    def exception(self, message: str, **kwargs: Any) -> None:
        """Log exception with structured data."""
        self.logger.exception(message, extra=kwargs)


def log_request(request_id: str, method: str, url: str, user_id: str = None) -> None:
    """
    Log HTTP request details.
    
    Args:
        request_id: Unique request identifier
        method: HTTP method
        url: Request URL
        user_id: User ID if authenticated
    """
    logger = get_logger("requests")
    logger.info(
        "HTTP Request",
        request_id=request_id,
        method=method,
        url=url,
        user_id=user_id,
    )


def log_response(request_id: str, status_code: int, response_time: float) -> None:
    """
    Log HTTP response details.
    
    Args:
        request_id: Unique request identifier
        status_code: HTTP status code
        response_time: Response time in seconds
    """
    logger = get_logger("requests")
    logger.info(
        "HTTP Response",
        request_id=request_id,
        status_code=status_code,
        response_time=response_time,
    )


def log_database_query(query: str, params: Dict[str, Any], duration: float) -> None:
    """
    Log database query details.
    
    Args:
        query: SQL query
        params: Query parameters
        duration: Query duration in seconds
    """
    logger = get_logger("database")
    logger.debug(
        "Database Query",
        query=query,
        params=params,
        duration=duration,
    )


def log_ai_request(model: str, prompt: str, response: str, duration: float) -> None:
    """
    Log AI service request details.
    
    Args:
        model: AI model used
        prompt: Input prompt
        response: AI response
        duration: Request duration in seconds
    """
    logger = get_logger("ai")
    logger.info(
        "AI Request",
        model=model,
        prompt_length=len(prompt),
        response_length=len(response),
        duration=duration,
    )


def log_security_event(event_type: str, user_id: str = None, details: Dict[str, Any] = None) -> None:
    """
    Log security-related events.
    
    Args:
        event_type: Type of security event
        user_id: User ID if applicable
        details: Additional event details
    """
    logger = get_logger("security")
    logger.warning(
        "Security Event",
        event_type=event_type,
        user_id=user_id,
        details=details or {},
    )


def log_audit_event(action: str, resource: str, user_id: str, details: Dict[str, Any] = None) -> None:
    """
    Log audit events for compliance.
    
    Args:
        action: Action performed
        resource: Resource affected
        user_id: User performing the action
        details: Additional audit details
    """
    logger = get_logger("audit")
    logger.info(
        "Audit Event",
        action=action,
        resource=resource,
        user_id=user_id,
        details=details or {},
    )
