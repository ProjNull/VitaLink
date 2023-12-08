from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = "UsersModel"

    User_ID = Column(
        Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    Name = Column(String, nullable=False)
    Email = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False)
    Description = Column(String, nullable=True)