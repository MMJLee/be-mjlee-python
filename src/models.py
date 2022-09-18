from sqlalchemy import Boolean, Column, Integer, String

from database import Base

# model for database


class Statement(Base):
    __tablename__ = 'statement'

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String, nullable=False)
    truth = Column(Boolean, nullable=False)
    backstory = Column(String, nullable=False)
    used = Column(Boolean, nullable=False)
