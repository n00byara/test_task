from sqlalchemy import Column, Integer, Text, REAL, ForeignKey
from sqlalchemy.orm import relationship

from constants import Constants
from db.models import Base

class ProductModel(Base):
    __tablename__ = Constants.PRODUCTS_TABLE.value

    id = Column(Integer, primary_key=True)
    sku = Column(Text, unique=True, nullable=True)
    name = Column(Text)
    price = Column(Integer)
    stories = Column(Integer)
    review_count = Column(Integer)
    rating_value = Column(REAL)
    comment = relationship("CommentModel")
    user_id = Column(Integer, ForeignKey(f"{Constants.USERS_TABLE.value}.id"))
    user = relationship("UserModel", back_populates=Constants.PRODUCT_FIELD.value)