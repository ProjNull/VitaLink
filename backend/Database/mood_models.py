from sqlalchemy import Column, ForeignKey, Integer, String

from Database.database import Base


class Mood(Base):
    __tablename__ = "Mood"

    idMood = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPatient = Column(Integer, ForeignKey("Patients.idPatient"), nullable=False)
    moodLevel = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
