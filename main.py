from decimal import Decimal
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: Decimal
    is_offer: Union[bool, None] = None

@app.get("/")
def index():
    return {
        "message": "Hello World!"
    }

@app.get("/{name}")
def say_hello(name: str):
    return {
        "message": f"Hello {name}"
    }

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "q": q,
    }

@app.put("/items/{item_id}")
def put_item(item_id: int, item: Item):
    return {
        "item_id": item_id,
        "name": item.name,
        "price": item.price,
    }
