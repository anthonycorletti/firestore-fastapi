import os
from datetime import datetime

from fastapi import APIRouter

router = APIRouter()
tags = ["health"]


@router.get("/healthcheck", tags=tags)
def healthcheck():
    return {
        "message": "healthy",
        "version": os.getenv("SHORT_SHA", "local"),
        "time": datetime.now()
    }
