import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(".env")

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

db = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db.query_property()
Base.metadata.create_all(engine)
