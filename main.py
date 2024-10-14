from fastapi import FastAPI

from config.settings import settings
from db.session import engine
#  because migration file will be created by alembic
# from db.base_class import Base


'''
create the tables in the database.
every time any model that will inherit the base class, they will be auto created once our app is starting up.
Comment NOTE: because migration file will be created by alembic
'''
# def create_tables():
#     Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()

@app.get("/")
def hello():
    return {"message": "Hello OP!!!"}
