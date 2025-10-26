from fastapi import FastAPI
from contextlib import asynccontextmanager
import structlog

from app.config import get_settings
from app.database import engine

settings = get_settings()


structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)

logger = structlog.getLogger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    logger.info("application_starting")
    yield
    logger.info("application_shutting_down")
    await engine.dispose()


# Create FastAPI app
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    lifespan=lifespan,
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Events Analytics API",
        "version": settings.api_version,
        "docs": "/docs"
    }
