"""Base Exception Classes for the Application"""
from typing import Optional, Any, Dict
from starlette.status import (HTTP_500_INTERNAL_SERVER_ERROR, 
                              HTTP_400_BAD_REQUEST,
                              HTTP_401_UNAUTHORIZED,
                              HTTP_403_FORBIDDEN,
                              HTTP_404_NOT_FOUND,
                              HTTP_409_CONFLICT,
                              HTTP_502_BAD_GATEWAY)


class AppException(Exception):
    """Base exception for all application exceptions"""
    
    def __init__(
        self,
        message: str,
        status_code: int = HTTP_500_INTERNAL_SERVER_ERROR,
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize exception with HTTP status and error details
        
        Args:
            message: Human-readable error message
            status_code: HTTP status code (default: 500)
            error_code: Internal error code for categorization
            details: Additional error details
        """
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}
        super().__init__(self.message)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary for API response"""
        return {
            "message": self.message,
            "error_code": self.error_code,
            "details": self.details,
        }


class ValidationException(AppException):
    """Base class for validation errors"""
    
    def __init__(
        self,
        message: str,
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message,
            status_code=HTTP_400_BAD_REQUEST,
            error_code=error_code or "VALIDATION_ERROR",
            details=details,
        )


class ResourceNotFoundException(AppException):
    """Base class for resource not found errors"""
    
    def __init__(
        self,
        resource: str,
        resource_id: Optional[str] = None,
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        message = f"{resource} not found"
        if resource_id:
            message += f" (ID: {resource_id})"
        
        super().__init__(
            message=message,
            status_code=HTTP_404_NOT_FOUND,
            error_code=error_code or "RESOURCE_NOT_FOUND",
            details=details or {"resource": resource, "id": resource_id},
        )


class AuthenticationException(AppException):
    """Base class for authentication errors"""
    
    def __init__(
        self,
        message: str = "Authentication failed",
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message,
            status_code=HTTP_401_UNAUTHORIZED,
            error_code=error_code or "AUTHENTICATION_ERROR",
            details=details,
        )


class AuthorizationException(AppException):
    """Base class for authorization errors"""
    
    def __init__(
        self,
        message: str = "Insufficient permissions",
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message,
            status_code=HTTP_403_FORBIDDEN,
            error_code=error_code or "AUTHORIZATION_ERROR",
            details=details,
        )


class ConflictException(AppException):
    """Base class for conflict errors (e.g., duplicate resources)"""
    
    def __init__(
        self,
        message: str,
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message,
            status_code=HTTP_409_CONFLICT,
            error_code=error_code or "CONFLICT",
            details=details,
        )


class DatabaseException(AppException):
    """Base class for database errors"""
    
    def __init__(
        self,
        message: str = "Database operation failed",
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message,
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            error_code=error_code or "DATABASE_ERROR",
            details=details,
        )

class ForbiddenException(AppException):
    """Base class for forbidden access errors"""
    
    def __init__(
        self,
        message: str = "Forbidden",
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message,
            status_code=HTTP_403_FORBIDDEN,
            error_code=error_code or "FORBIDDEN",
            details=details,
        )

class ExternalServiceException(AppException):
    """Base class for external service errors"""
    
    def __init__(
        self,
        service_name: str,
        message: str = "External service error",
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=f"{service_name}: {message}",
            status_code=HTTP_502_BAD_GATEWAY,
            error_code=error_code or "EXTERNAL_SERVICE_ERROR",
            details=details or {"service": service_name},
        )
