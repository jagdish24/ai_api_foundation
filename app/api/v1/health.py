
from fastapi import APIRouter, status
from datetime import datetime, UTC
health_router = APIRouter(prefix="/health", tags=["Health"])

@health_router.get("/", status_code=status.HTTP_200_OK)
def health_check():
    """
    Basic Health check point
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now()
    }

def liveliness():
    pass