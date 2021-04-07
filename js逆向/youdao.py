from hashlib import md5
import requests
import time
import random

"""
salt: 16171725892584
sign: 333cabc52a84b170ce90e28eafd9a205
lts: 1617172589258
bv: cda1e53e0c0eb8dd4002cefc117fa588
"""
# s = "fanyideskweb"  + "16171734238674" +"Tbh5E8=q6U3EXe+&L[4c@"
# md = md5()
# md.update(s.encode())
# a = md.hexdigest()
# print(a)
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
    # "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Referer": "http://fanyi.youdao.com/",
    # "Origin":"http://fanyi.youdao.com",
    "Cookie": "OUTFOX_SEARCH_USER_ID=-512169720@10.168.8.63; OUTFOX_SEARCH_USER_ID_NCOO=1898612054.641503; P_INFO=null; ANTICSRF=cleared; NTES_OSESS=cleared; S_OINFO=; JSESSIONID=aaaWnOQTzwSnBarUo8gIx; ___rl__test__cookies=1617174331643",
     "X-Requested-With": "XMLHttpRequest"

}
word = input("输入要翻译的字: ")
lts = str(int(time.time()*1000))
salt = lts + str(random.randint(0,9))
s =  "fanyideskweb"  + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
md = md5()
md.update(s.encode())
sign = md.hexdigest()
bv = 'cda1e53e0c0eb8dd4002cefc117fa588'
post_data = {
    "i": word ,
    "from": 'AUTO',
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": salt ,
    "sign": sign,
    "lts": lts ,
    "bv": bv,
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION"
}
html = requests.post(url=url, headers=headers, data=post_data)
print(html.json())

