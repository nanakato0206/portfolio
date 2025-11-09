from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/books")
def get_books(q: str = Query(..., description="検索キーワード")):

    url = f'https://www.googleapis.com/books/v1/volumes?q={q}'

    res = requests.get(url)

    status = res.status_code

    result = res.json()

    books = []
    for item in result.get("items", []):
        info = item.get("volumeInfo", {})
        books.append({
            "id": item.get("id"),  
            "kind": item.get("kind"), 
            "title": info.get("title"),
            "publishedDate": info.get("publishedDate"),
            "description": info.get("description")
        })

    return {
        "status_code": status,
        "query": q,
        "results_count": len(books),
        "books": books
    }
