from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///DataBase.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)