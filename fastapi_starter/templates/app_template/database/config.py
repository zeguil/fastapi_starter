from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "banco.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Caso use outro banco
# Defina as variáveis de configuração do banco de dados

# DB_USER = 'seu_usuario'
# DB_PASSWORD = 'sua_senha'
# DB_HOST = 'localhost'
# DB_PORT = '3306'
# DB_NAME = 'seu_banco'

#mysql --  pip install mysqlclient
# DATABASE_URL = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#postgres -- pip intall psycopg2
# DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


