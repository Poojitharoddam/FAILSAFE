# ==========================
# PostgreSQL Database Connection
# ==========================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Change these credentials if needed

DATABASE_URL = (
    "postgresql://postgres:password@localhost:5432/failsafe_db"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependency


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()