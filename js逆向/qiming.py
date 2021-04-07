import execjs
import requests
import json

with open("./qiming.js", encoding="utf8") as f:
    js_file = f.read()

def get():
    # url = "https://vipapi.qimingpian.com/search/productNewList"
    # url = "https://vipapi.qimingpian.com/HomePage/provinceInvestChart"
    url = "https://vipapi.qimingpian.com/DataList/investEventVip"
    # url = "https://vipapi.qimingpian.com/DataList/investmentTotalVip"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Origin": "https://www.qimingpian.cn",
        "X-Powered-By": "PHP/5.5.7"
    }
    data = {
        "page": 1,
        "num": 20,
        # "unionid":""
    }
    res = requests.post(url, data=data, headers=headers)
    return res.json().get("encrypt_data")
data = get()

result = execjs.compile(js_file).call("o", data)
print(json.loads(result))
lst_result = json.loads(result)["list"]
# with open("qiming.txt", "a+", encoding="utf8") as f:
# #     for dic in lst_result:
# #         f.write(json.dumps(dic, ensure_ascii=False))
# #         f.write("\n")