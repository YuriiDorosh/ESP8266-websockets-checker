import asyncio
import logging

import uvicorn
from api.routes import router as v1_router
from api.ws.ligth import init_websocket_server
from bot import init_bot, start_polling
from config.redis import RedisConfig
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

logging.basicConfig(level=logging.INFO)

redis_config = RedisConfig()

router = APIRouter(
    prefix="api",
    tags=["api"],
)

router.include_router(v1_router)

app = FastAPI(
    title="FastAPI Starter Project",
    description="FastAPI Starter Project",
    version="1.0",
    docs_url="/api/docs/",
    redoc_url="/api/redoc/",
    openapi_url="/api/openapi.json",
    default_response_class=UJSONResponse,
)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    redis = aioredis.from_url(
        redis_config.get_url(), encoding="utf8", decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    init_bot()
    init_websocket_server(app)
    asyncio.create_task(start_polling())


@app.on_event("shutdown")
async def on_shutdown():
    logging.info("Shutting down")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
