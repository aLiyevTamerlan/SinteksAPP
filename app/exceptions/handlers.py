"""Exception Handlers for FastAPI Integration"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from .base import AppException


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all exception handlers with FastAPI app
    
    Usage:
        from app.exceptions.handlers import register_exception_handlers
        from app.main import app
        
        register_exception_handlers(app)
    """
    
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
        """Handle custom application exceptions"""
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.message,
                "error_code": exc.error_code,
                "details": exc.details,
            },
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        """Handle Pydantic validation errors"""
        errors = []
        for error in exc.errors():
            errors.append({
                "field": ".".join(str(x) for x in error["loc"][1:]),
                "message": error["msg"],
                "type": error["type"],
            })
        
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "detail": "Validation error",
                "error_code": "VALIDATION_ERROR",
                "details": {
                    "validation_errors": errors,
                },
            },
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        """Handle unexpected exceptions"""
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal server error",
                "error_code": "INTERNAL_SERVER_ERROR",
                "details": {
                    "type": type(exc).__name__,
                },
            },
        )
