from datetime import datetime

from fastapi import APIRouter

from firestorefastapi import __version__
from firestorefastapi.logger import logger
from firestorefastapi.schemas.health import HealthcheckResponse

router = APIRouter()
tags = ["health"]


@router.get("/healthcheck", response_model=HealthcheckResponse, tags=tags)
def healthcheck() -> HealthcheckResponse:
    message = "healthy"
    logger.debug(message)
    return HealthcheckResponse(
        message=message,
        version=__version__,
        time=datetime.now(),
    )
