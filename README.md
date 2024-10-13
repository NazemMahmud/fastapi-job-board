## Technology Stacks
- **An asynchronous web server to execute**: There are some like, **Uvicorn**, **Hypercone** etc.
Here, **uvicorn** is used.
- **Unit test**: `pytest`
- **ORM**: `SQLAlchemy`. There are others like _Tortoise_, _Peewee_, _PonyORM_ for non SQL databases. \n
This ORM supports async queries.
- **Database**: `PostgreSQL`
- **Database Server**: `Supabase`
- **Web App (_HTML Screens_)**: `Jinja2`
- Data Validation Helper: `pydantic`

## Virtual Environment (optional)
It is useful because instead of installing globally in your PC, it will only install inside specific virtual environment.\n
You can delete it easily.
- Create a virtual environment and activate it.
```shell
source virtualEnvironmentFolderName/Scripts/activate
```

## Supabase
Here, supabase is used as postgresql database host server. \
In this way, we don't have to install postgresql or pgadmin or dbeaver or other DB manager in our local.


## Installation
Install all from `requirements.txt` file. \
**NOTE:** Before installation, check `requirements.txt` file for further note based on OS

```shell
pip install -r requirements.txt
```

## Run Project
In your terminal, run command:
```shell
fastapi dev main.py
```

Or,
```shell
uvicorn main:app --reload
```


## Package details
- `fastapi`: To use FastAPI
- `fastapi-cli`: To run/start FastAPI project from cli
- `uvicorn`: asynchronous web server to execute
- `pydantic`: Data validation
- `SQLAlchemy`: ORM for python
- `psycopg2`: PostgreSQL database adapter for the Python programming language.
- `python-dotenv`: keep/track data from `.env` file
- `supabase`: Make host and control PostgreSQl easier