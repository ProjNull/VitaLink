from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from Database.database import Base

class Employees(Base):
    __tablename__ = 'Employees'

    idEmployee = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    firstName = Column(String, nullable = False)
    lastName = Column(String, nullable = False)
    nickname = Column(String, nullable = True)
    password = Column(String, nullable = False)
    dateOfBirth = Column(Date, nullable = False)
    isAdmin = Column(Boolean, nullable = False, default = False)

class AccessToPatient(Base):
    __tablename__ = 'AccessToPatient'

    idEmployee = Column(Integer, ForeignKey('Employees.idEmployees'), nullable = False)
    idPatient = Column(Integer, ForeignKey('Patients.idPatient'), nullable = False)
    

class Patients(Base):
    __tablename__ = 'Patients'

    idPatient = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    firstName = Column(String, nullable = False)
    lastName = Column(String, nullable = False)
    dateOfBirth = Column(Date, nullable = False)
    passcode = Column(String, nullable = True) #not implemented says štefan