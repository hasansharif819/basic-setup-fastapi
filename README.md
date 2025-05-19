# FastAPI

## Project Setup
* Create virtual env
```bash
  $ python3 -m venv env_name
```
  
* Activate the virtual env
  ```bash
  $ source env_name/bin/activate
  ```

* Dependency Install

```bash
  $ pip install fastapi uvicorn SQLAlchemy pydantic psycopg2-binary passlib email_validator cryptography bcrypt alembic
```

```bash
  $ pip freeze > requirements.txt
```

* database setup

* Migration

```bash
  $ alembic init alembic
```
* Go to alembic.ini file and change the database url
* alembic --> env.py
*             [from database.db import Base]
*             [target_metadata = Base.metadata]

```bash
  $ alembic revision --autogenerate -m "user migration"
  $ alembic upgrade head
```

## Finally Run 

```bash
  $ uvicorn main:app --reload --port 5000 --host 0.0.0.0
```
