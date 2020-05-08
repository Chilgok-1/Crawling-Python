from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("http://www.welkeepsmall.com/shop/shopdetail.html?branduid=1007212&xcode=023&mcode=002&scode=&special=1&GfDT=bW93UQ%3D%3D")
try :
    Buy_me = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.prd-btns > a.btn_buy.fe"))
        ).text
    print(Buy_me)   
    if Buy_me == 'BUY IT NOW':
        os.system('gmail_auto.py')
finally:
    driver.quit()