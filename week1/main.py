from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Item(BaseModel):

    name:str
    price:float
    description: Union[str,None]=None


@app.get("/")

def read_root():
    return {"message":"サブAPIです"}   

@app.post("/items/")
def create_item(item:Item):
    print(f"データを登録します: {item.name},{item.price},{item.description}")
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int , name: str, price: float):
    return {"item_id": item_id, "name": name, "price": price}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}
