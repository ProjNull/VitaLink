from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from Database.database import Base

class Mood(Base):
    __tablename__ = 'Mood'

    # WIP not done
    
    # idAccess = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    # idEmployee = Column(Integer, ForeignKey('Employees.idEmployees'), nullable = False)
    # idPatient = Column(Integer, ForeignKey('Patients.idPatient'), nullable = False)
    # isPrimaryNurse = Column(Boolean, nullable = False, default = False)