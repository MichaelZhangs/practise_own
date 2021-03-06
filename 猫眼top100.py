# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:24:58 2019

@author: PC
"""
import urllib.request

import re

class MaoYanSpider(object):
    
    def __init__(self):
        self.header = {"User-Agent":"Mozilla/5.0 (Platform; Encryption; OS-or-CPU; Language)"}
        self.page = 1
        self.offset = 0
        self.baseurl = "http://maoyan.com/board/4?offset="
        
    #获取html源码
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.header)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html
    #正则解析html源码
    def parsePage(self,html):
        reg='<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?</div>'
        p = re.compile(reg,re.S)
    
        content_list = p.findall(html)
        return content_list
        #[("霸王别姬","张国荣","1993")]
    #写入文件
    def writePage(self,content_list):
        for m_tuple in content_list:
            for n_str in m_tuple:
                with open("猫眼电影.txt",'a',encoding="utf-8") as f:
                    f.write(n_str.strip()+"\n")
            with open("猫眼电影.txt","a",encoding="utf-8") as f:
                f.write("\n\n")
    #主函数
    def workOn(self):
        while True:
        
            url=self.baseurl+str(self.offset)
            print("正在爬取第%d页" % self.page)
            #获取源码
            html = self.getPage(url)
            #解析源码
            content_list = self.parsePage(html)
            #写入源码
            self.writePage(content_list)
            print("第%d页爬取成功"%self.page)

            ch = input("是否继续爬取(y/n):")
            if ch.strip().lower() == "y":
                self.offset +=10
                self.page +=1
            else:
                print("爬取结束")
                break
            
            
if __name__=="__main__":
    spider = MaoYanSpider()
    spider.workOn()
