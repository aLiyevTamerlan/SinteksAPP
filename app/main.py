"""FastAPI Application Entry Point - Async"""
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api import router as api_router




# Initialize FastAPI app
app = FastAPI(
    title="Sinteks API",
    debug=settings.DEBUG
)



# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register exception handlers

# Include API routers
app.include_router(api_router, prefix="/api")


