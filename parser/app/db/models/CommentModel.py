from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from constants import Constants
from db.models import Base

class CommentModel(Base):
    __tablename__ = Constants.COMMENTS_TABLE.value

    id= Column(Integer, primary_key=True)
    text = Column(Text)
    post_id = Column(Text, unique=True)
    product_id = Column(Integer, ForeignKey(f"{Constants.PRODUCTS_TABLE.value}.id"))
    product = relationship("ProductModel", back_populates=Constants.COMMENT_FIELD.value)