## Technology Stacks
- **An asynchronous web server to execute**: There are some like, **Uvicorn**, **Hypercone** etc.
Here, **uvicorn** is used.
- **Unit test**: `pytest`
- **ORM**: `SQLAlchemy`. There are others like _Tortoise_, _Peewee_, _PonyORM_ for non SQL databases. \n
This ORM supports async queries.
- **Database**: `PostgreSQL`
- **Web App (_HTML Screens_)**: `Jinja2`

## Virtual Environment (optional)
It is useful because instead of installing globally in your PC, it will only install inside specific virtual environment.\n
You can delete it easily.
- Create a virtual environment and activate it.
```shell
source virtualEnvironmentFolderName/Scripts/activate
```


## Installation
Install all from `requirements.txt` file
```shell
pip install -r requirements.txt
```

## Run Project
In your terminal, run command:
```shell
fastapi dev main.py
```