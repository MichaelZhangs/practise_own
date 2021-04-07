import requests
import re

start_url = "http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc"
url = "http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList"


res = requests.get(start_url)
cookies =res.cookies
print(res.text)

cookie = cookies.get("XSRF-TOKEN")
session = cookies.get("szxx_session")
csrf = re.findall(r"var _CSRF =(.*?);", res.text)
print(csrf)
print(cookie)
print(session)
print(csrf)

headers = {
    "Cookie":"zh_choose=n;XSRF-TOKEN={};szxx_session={}".format(cookie,session),
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Referer": "http://www.zjmazhang.gov.cn",
    "X-CSRF-TOKEN":"{}".format(csrf)
}
print(headers)

form_data = {
    "offset":"0",
    "limit":"20",
    "site_id":"759010"
}

resp = requests.post(url=url, headers=headers, data=form_data)
print(resp.json())