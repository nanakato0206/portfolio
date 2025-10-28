from fastapi import FastAPI
# fastAPIクラスをインポート

app = FastAPI()


@app.get("/")
# デコレータ　リクエストメゾットがGETでURLがドメインまでのリクエストが来た時に呼び出される
def read_root():
    return {"message":"サブAPIです"}   

@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}

@app.put("/items/{item_id}")
def update_item(item_id: int , name: str, price: float):
    return {"name": name, "price": price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}
