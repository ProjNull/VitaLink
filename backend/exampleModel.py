from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Employees(Base):
    __tablename__ = 'Employees'

    idEmployees = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    firstName = Column(String, nullable = False)
    lastName = Column(String, nullable = False)
    password = Column(String, nullable = False)

class Patients(Base):
    __tablename__ = 'Patients'

    idPatient = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    idEmployees = Column(Integer, ForeignKey('Employees.idEmployees'), nullable = True)
    firstName = Column(String, nullable = False)
    lastName = Column(String, nullable = False)
    passcode = Column(String, nullable = True) #not implemented says štefan