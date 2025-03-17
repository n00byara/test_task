import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy.engine import Engine
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session

from configuration import config
from db.models import Base
from db.models import CommentModel
from db.models.ProductModel import ProductModel
from db.models.UserModel import UserModel

pg_conf = config.postgres

class DataBase:
    engine: Engine = None
    connect: Connection = None
    metadata: MetaData = None

    def __init__(self):
        self.engine = db.create_engine(
            f"postgresql+psycopg2://{pg_conf.username}:{pg_conf.userpassword}@{pg_conf.host}:{pg_conf.port}/{pg_conf.database}"
        )
        self.connect = self.engine.connect()
        self.metadata = db.MetaData()

        Base.metadata.create_all(self.engine)

    def _get_user(self, session: Session, user_model) -> UserModel:
        return session.query(UserModel).filter(UserModel.email.like(user_model.email)).first()

    def _get_product(self, session: Session, product_data) -> ProductModel:
        return session.query(ProductModel).filter(ProductModel.sku.like(product_data["sku"])).first()

    def _get_comment(self, session: Session, comment_data) -> CommentModel:
        return session.query(CommentModel).filter(CommentModel.post_id.like(comment_data["post_id"])).first()

    def add_user(self, user_model, user_data):
        with Session(bind=self.engine) as session:
            if not self._get_user(session, user_model):
                session.add(UserModel(email=user_data["email"], firstname=user_data["firstname"], lastname=user_data["lastname"], city=user_data["city"]))
                session.commit()


    def add_product(self, user_model, product_data):
        with Session(bind=self.engine) as session:
            user = self._get_user(session, user_model)

            if user and not self._get_product(session, product_data):
                product = ProductModel(sku=product_data["sku"], name=product_data["name"], price=product_data["price"], stories=product_data["stores"], review_count=product_data.get("review_count"), rating_value=product_data.get("rating_value"), user_id=user.id)
                session.add(product)
                session.commit()

    def add_comment(self, product_data, comment_data):
        with Session(bind=self.engine) as session:
            product = self._get_product(session, product_data)
            
            if product and not self._get_comment(session, comment_data):
                session.add(CommentModel(post_id=comment_data["post_id"], text=comment_data["text"], product_id=product.id))
                session.commit()