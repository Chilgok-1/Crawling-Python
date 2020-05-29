from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome('/Users/yun/Desktop/크롤링/chromedriver')
driver.get('https://lib.skku.edu/#/search/monthly-book-search/si?all=0&max=100')

time.sleep(5)

libs = driver.find_elements_by_css_selector('span.ikc-item-branch')
name = []
i=0

for lib in libs:
    name.append(lib.text)

buttons = driver.find_elements_by_css_selector("a.hidden-xs > span.k-icon.k-i-collapse")
i = 0
for button in buttons:
    time.sleep(0.05)
    if(name[i] == "중앙학술정보관"):
        button.click()
    i = i+1
