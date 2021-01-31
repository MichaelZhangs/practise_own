# encoding:utf8
import requests
import json
from lxml import etree
from queue import Queue
import threading
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/text/{}"
        self.headers = {
            "Referer": "http://www.qiushibaike.com",
            "User-Agent": "Mozilla/5.0 (Platform; Encryption; OS-or-CPU; Language)"
        }
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()
    def get_url(self):
        # return [self.url_temp.format(i) for i in range(1, 14)]
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self,):
        while True:
            url = self.url_queue.get()
            print(url)
            resp = requests.get(url, headers=self.headers)
            # return resp.text
            self.html_queue.put(resp.text)
            self.url_queue.task_done()  #不加回卡住

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@class='col1 old-style-col1']/div")
            content_lst = []
            for div in div_list:
                item = {}

                item["content"] = div.xpath(".//div[@class='content']/span/text()")
                item["content"] = [i.replace("\n", "") for i in item["content"]]

                item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
                item["author_gender"] = item["author_gender"][0].replace("Icon", "") if len(
                    item["author_gender"]) > 0 else None

                item["author_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
                item["author_age"] = item["author_age"][0] if len(item["author_age"]) > 0 else None

                item["author_pic"] = div.xpath(".//div[@class='author clearfix']/a/img/@src")
                item["author_pic"] = "https://" + item["author_pic"][0] if len(item["author_pic"]) > 0 else None

                item["vote_number"] = div.xpath(".//span[@class='stats-vote']/i/text()")
                item["vote_number"] = item["vote_number"][0] if len(item["vote_number"]) > 0 else None

                item["review_count"] = div.xpath(".//span[@class='stats-comments']/a/i/text()")
                item["review_count"] = item["review_count"][0] if len(item["review_count"]) > 0 else None
                content_lst.append(item)
            # return content_lst
            self.content_queue.put(content_lst)
            self.html_queue.task_done()

    def save(self):
        while True:
            content_list = self.content_queue.get()
            with open("多线程糗事.json", "a", encoding="utf8") as f:
                for data in content_list:
                    f.write(json.dumps(data, ensure_ascii=False))
                    f.write("\n")
            # for data in content_list:
            #     print(data)
            self.content_queue.task_done()
    def run(self):
        thread_list = []
        t_url = threading.Thread(target=self.get_url)
        thread_list.append(t_url)
        for i in range(3):
            t_parse =  threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        for i in range(2):
            t_html =  threading.Thread(target=self.get_content_list)
            thread_list.append(t_html)
        t_save = threading.Thread(target=self.save)
        thread_list.append(t_save)

        for t in  thread_list:
            t.setDaemon(True) #吧子线程设置为守护线程，该线程不重要主线程结束，子线程结束
            t.start()
        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join() #让主线程等待阻塞，等待队列的任务完成之后在完成
        print("主线程结束")

if __name__ == '__main__':
    qu = QiubaiSpider()
    qu.run()
