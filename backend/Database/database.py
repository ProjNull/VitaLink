from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.state import InstanceState

Base = declarative_base()

engine = create_engine("sqlite:///DataBase.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)