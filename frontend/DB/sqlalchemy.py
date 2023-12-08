from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Zamestnanci(Base):
    __tablename__ = 'Zamestnanci'

    idZamestnance = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    firstName = Column(String, nullable = False)
    lastName = Column(String, nullable = False)
    password = Column(String, nullable = False)

class Pacienti(Base):
    __tablename__ = 'Pacienti'

    idPacienta = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    idZamestnance = Column(Integer, ForeignKey('Zamestnanci.idZamestnance'), nullable = True)
    firstName = Column(String, nullable = False)
    lastName = Column(String, nullable = False)
    passcode = Column(String, nullable = True) #not implemented says štefan