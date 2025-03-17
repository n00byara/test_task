from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from constants import Constants
from db.models import Base

class UserModel(Base):
    __tablename__ = Constants.USERS_TABLE.value

    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=True, nullable=True)
    firstname = Column(Text)
    lastname = Column(Text)
    city = Column(Text)
    product = relationship("ProductModel")