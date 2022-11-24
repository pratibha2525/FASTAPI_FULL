from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('postgres:///./flask_db', echo=True)
DATABASE_URL = "postgresql://postgres:admin@localhost/flask_db"

engine = create_engine(DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = sessionlocal()

    try:
        yield db
    finally:
        db.close()
