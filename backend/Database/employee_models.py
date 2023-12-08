from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from Database.database import Base

class Employees(Base):
    __tablename__ = 'Employees'

    idEmployee = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    firstName = Column(String, nullable = False)
    lastName = Column(String, nullable = False)
    nickname = Column(String, nullable = True)
    email = Column(String, nullable = False)
    nick = Column(String, nullable = True)
    password = Column(String, nullable = False)
    dateOfBirth = Column(Date, nullable = False)
    isAdmin = Column(Boolean, nullable = False, default = False)
