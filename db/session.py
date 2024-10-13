from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database url is: ", SQLALCHEMY_DATABASE_URL)

# entry point for any SQL engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)