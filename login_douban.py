#encoding:utf8
from selenium import  webdriver
import time


driver = webdriver.Chrome()
driver.get('https://www.douban.com/')


iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

driver.find_element_by_class_name('account-tab-account').click()
driver.find_element_by_id('username').send_keys("*******")
driver.find_element_by_id('password').send_keys("***********")
driver.find_element_by_class_name('btn-account').click()
time.sleep(5)



# driver.quit()
#
# driver.find_element_by_id("username").send_keys("*********")
# driver.find_element_by_id("password").send_keys("********")
# time.sleep(3)
# driver.find_element_by_class_name("btn-account").click()

