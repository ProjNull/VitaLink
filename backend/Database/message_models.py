from datetime import datetime

from Database.database import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String


class Messages(Base):
    __tablename__ = "Messages"

    idMessage = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmployee = Column(Integer, ForeignKey("Employees.idEmployee"), nullable=False)
    idPatient = Column(Integer, ForeignKey("Patients.idPatient"), nullable=False)
    senderIsPatient = Column(Boolean, nullable=False)
    replyTo = Column(Integer, ForeignKey("Messages.idMessage"), nullable=True)
    content = Column(String, nullable=False)
    createdAt = Column(DateTime, nullable=False, default=datetime.now())
