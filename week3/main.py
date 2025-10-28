import requests
import json

res = requests.get('https://www.googleapis.com/books/v1/volumes?q=python')
print("ステータスコード:", res.status_code) 

result = res.json()
print(result)

print(json.dumps(result, indent=4,ensure_ascii=False))