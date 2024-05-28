import uvicorn
from typing import Dict
from models.model import *
from fastapi import FastAPI
from sqlalchemy import inspect
from database.config import Base, engine


inspector = inspect(engine)

# Verificar se as tabelas já existem no banco de dados
existing_tables = inspector.get_table_names()

# Cria as tabelas se elas não existirem
if not existing_tables:
    Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def index() -> Dict:
    return {"acesse:": "localhost:8080/docs"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="localhost")