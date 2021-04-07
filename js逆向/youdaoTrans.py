from hashlib import md5
import requests
import time
import random

class YoudaoTrans:
    def __init__(self, word=None):
        self.headers ={
    # "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Referer": "http://fanyi.youdao.com/",
    "Cookie": "OUTFOX_SEARCH_USER_ID=-512169720@10.168.8.63; OUTFOX_SEARCH_USER_ID_NCOO=1898612054.641503; P_INFO=null; ANTICSRF=cleared; NTES_OSESS=cleared; S_OINFO=; JSESSIONID=aaaWnOQTzwSnBarUo8gIx; ___rl__test__cookies=1617174331643",
     "X-Requested-With": "XMLHttpRequest"

}
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.word = word
        self.bv = "cda1e53e0c0eb8dd4002cefc117fa588" #用md5对userAgent 下的 / 后的字段进行md5加密

    def getSalt(self):
        lts = str(int(time.time() * 1000))
        salt = lts + str(random.randint(0, 9))
        s = "fanyideskweb" + self.word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        md = md5()
        md.update(s.encode())
        sign = md.hexdigest()

        return lts, salt,sign

    def merge(self):
        lts, salt, sign = self.getSalt()
        post_data = {
            "i": self.word,
            "from": 'AUTO',
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": self.bv,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION"
        }
        return  post_data

    def trans(self):
        data = self.merge()
        html = requests.post(url=self.url, headers=self.headers, data=data)
        print(html.json().get("translateResult"))

if __name__ == '__main__':
    word = input("输入要翻译的内容：")
    youdao = YoudaoTrans(word)
    youdao.trans()
