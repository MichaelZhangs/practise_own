from selenium import  webdriver
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    'Connection': 'keep-alive',
}

driver = webdriver.Chrome(r"E:\chromedriver.exe")
print(driver)
url = "https://i04piccdn.sogoucdn.com/44fde94811a386be"
# url = "https://img1.baidu.com/it/u=3246628741,3439955235&fm=26&fmt=auto"
# login_url = "https://www.baidu.com"
login_url = "https://www.sogou.com/"
driver.get(url=login_url)
cookis = driver.get_cookies()
print("cookis = ", cookis)
# data = driver.get(url)
# print(driver.get_cookies())
cookie = ";".join([item["name"] + "=" + item["value"] + "" for item in cookis])
print("cookie = ", cookie)
sess = requests.Session()
headers["Cookie"] = cookie
for c in cookis:
    sess.cookies.set(c["name"], c["value"])
# sess.headers = headers
content = sess.get(url, headers=headers)

print(content.status_code)
open("aa.jpg", "wb").write(content.content)
driver.close()