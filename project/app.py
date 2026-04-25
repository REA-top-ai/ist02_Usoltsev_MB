from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from init_db import create_db_if_not_exist
from models import create_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_if_not_exist()
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)