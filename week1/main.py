from fastapi import FastAPI
# fastAPIクラスをインポート
from pydantic import BaseModel
# fastAPIクラスをインポート
from typing import Union

app = FastAPI()

class Item(BaseModel):
    # itemクラスのBaseModelを継承
    name:str
    price:float
    description: Union[str,None]=None
    # unionは複数のデータ型を宣言できる

@app.get("/")
# デコレータ　リクエストメゾットがGETでURLがドメインまでのリクエストが来た時に呼び出される
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
