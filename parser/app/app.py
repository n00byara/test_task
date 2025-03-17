from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import db
from parser import Parser
from models import UserModel
from db.models import ProductModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/get_user_info")
async def user_info(user: UserModel):
    parser = Parser(user)
    user_info: dict = parser.get_user_info()
    db.add_user(user, user_info)
    
    return user_info

@app.post("/get_grid_list")
async def user_info(user: UserModel):
    parser = Parser(user)

    grid_list: list = parser.get_grid_list()
    
    for product in grid_list:
        db.add_product(user, product)
        for comment in product.get("comments", []):
            db.add_comment(product, comment)

    return grid_list