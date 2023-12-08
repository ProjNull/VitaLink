from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from .database import Base

class AccessToPatient(Base):
    __tablename__ = "AccessToPatient"

    idAccess = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmployee = Column(Integer, ForeignKey("Employees.idEmployees"), nullable=False)
    idPatient = Column(Integer, ForeignKey("Patients.idPatient"), nullable=False)
    isPrimaryNurse = Column(Boolean, nullable=False, default=False)


class Patients(Base):
    __tablename__ = "Patients"

    idPatient = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    nick = Column(String, nullable=True)
    dateOfBirth = Column(Date, nullable=False)
    password = Column(String, nullable=True)  # not implemented says štefan
