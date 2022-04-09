import requests

resp = requests.get("http://127.0.0.1:8003/?a=3&b=4")
print(resp.text)