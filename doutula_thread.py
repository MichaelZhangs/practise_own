# encoding:utf8
import requests
from lxml import etree
from urllib import request
import os
import time
from queue import Queue
import threading

class Producer(threading.Thread):
    headers = {
        "Referer": "https://www.doutula.com",
        "User-Agent": "Mozilla/5.0 (Platform; Encryption; OS-or-CPU; Language)",
        "proxy": "http://120.232.150.100:80"
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_que = Queue(10)
        self.img_que = Queue(20)

    def run(self):
        while True:
            if self.img_que.empty() and self.page_que.empty():
                break
            url, file_name = self.img_que.get()
            print("-------")
            print(url,file_name)
            request.urlretrieve(url,"doutula/thread/{}".format(file_name))


    def getUrl(self):
        url = "https://www.doutula.com/photo/list/?page={}"
        url_list = (url.format(i) for i in range(5))
        for u in url_list:
            self.page_que.put(u)


    def parseUrl(self):
        while True:
            url = self.page_que.get()
            if self.page_que.empty():
                break
            print(url)
            content = requests.get(url, headers=self.headers)
            text = content.text
            self.getData(text)

    def getData(self,text):
        html = etree.HTML(text)
        images = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        # print(images)
        for img in images:
            # if img.split(".")[-1] != "gif":
            # print(etree.tostring(img).decode())
            img_url = img.get("data-original")
            alt = img.get("alt")
            backprefix = os.path.splitext(img_url)[-1]  # 安装后缀名切割 得到时个元组
            # backprefix = img_url.split(".")[-1]
            file_name = alt + backprefix
            if not alt or alt == "?":
                file_name = os.path.split(img_url)[-1]
            # request.urlretrieve(img_url, "doutula/{}".format(file_name))
            print(file_name)

            self.img_que.put((img_url, file_name))

def main():
    p = Producer()
    for i in range(2):
        t = threading.Thread(target=p.getUrl)
        t.start()
    for i in range(5):
        t = threading.Thread(target=p.parseUrl)
        t.start()
    for i in range(4):
        t = threading.Thread(target=p.run)
        t.start()

    # page_que = Queue(10)
    # img_que = Queue(20)
    # for x in range(5):
    #     t = Producer(page_que, img_que)
    #     t.start()

if __name__ == '__main__':
    start = time.time()
    main()
    print("end = ", time.time() - start)
