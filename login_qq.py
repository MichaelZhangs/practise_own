#encoding:utf8
from selenium import webdriver
import time

from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
time.sleep(4)
#输入密码

driver.maximize_window()

driver.find_element_by_id("qqLoginTab").click()
# iframe = driver.find_element_by_tag_name("iframe")
# print(iframe)
driver.switch_to.frame("login_frame")
driver.find_element_by_id("u").send_keys("879966081")
time.sleep(2)
driver.find_element_by_id("p").send_keys("ZHANG9311520")

driver.find_element_by_id("login_button").click()
time.sleep(3)
