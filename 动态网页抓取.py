#/usr/bin/python
#-*- coding:UTF-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# caps = webdriver.DesiredCapabilities().FIREFOX
# caps["marionette"] = False

driver = webdriver.Firefox()

driver.get("https://zh.airbnb.com/s/Shenzhen--China/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJkVLh0Aj0AzQRyYCStw1V7v0&click_referer=t%3ASEE_ALL%7Csid%3A1431bb7e-15b5-4a56-beb0-a6c0e90773c8%7Cst%3AMAGAZINE_HOMES&title_type=MAGAZINE_HOMES&query=Shenzhen%2C%20China&s_tag=OGL9dqGo",timeout=10)

#获取整体房间信息
rent_list = driver.find_elements_by_css_selector('div._14csrlku')

#获取点评参数：
for eachhouse in rent_list:
    # comment = eachhouse.find_element_by_css_selector('div._36rlri')
    # comment = comment.text
    price = eachhouse.find_element_by_css_selector('span._1dfubau0')
    price = price.text

    print(price)


