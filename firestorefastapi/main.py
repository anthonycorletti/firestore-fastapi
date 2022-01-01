import os

from fastapi import FastAPI

from v1.routers import health, item

os.environ["TZ"] = "UTC"

title_detail = os.getenv("PROJECT_ID", "Local")
version = os.getenv("SHORT_SHA", "local")
api = FastAPI(title=f"Firestore FastAPI: {title_detail}", version=version)

# /
api.include_router(health.router)

# /v1
api_v1_prefix = "/v1"
api.include_router(item.router, prefix=api_v1_prefix)
