from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date, DateTime, func
from sqlalchemy.orm import relationship

from Database.database import Base

class Messages(Base):
    __tablename__ = 'Messages'

    idMessage = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    idEmployee = Column(Integer, ForeignKey('Employees.idEmployees'), nullable = False)
    idPatient = Column(Integer, ForeignKey('Patients.idPatient'), nullable = False)
    senderIsPatient = Column(Boolean, nullable = False)
    replyTo = Column(Integer, ForeignKey('Messages.idMessage'), nullable = True)
    content = Column(String, nullable = False)
    createdAt = Column(DateTime, server_default=func.now())