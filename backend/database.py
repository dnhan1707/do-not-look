import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://myuser:mypassword@db:5432/fun_project_db"
)

engine = create_async_engine(DATABASE_URL, echo=True)

# Create temp sessions for each request
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

# FastAPI Dependency to yield a session and close it when the request is done
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session