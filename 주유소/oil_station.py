from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("http://v4.map.naver.com")
driver.find_elements_by_css_selector('.btn_close')[1].click()

search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("칠곡 주유소")
search_button = driver.find_element_by_css_selector('#header > div.sch > fieldset > button')
search_button.click()

name=[]
addr=[]
price_detail=[]
price_detail2=[]

stores = driver.find_elements_by_css_selector("div.lsnx")

for store in stores:
    # 세부 데이터 수집
    name.append(store.find_element_by_css_selector("dt > a").text)
    addr.append(store.find_element_by_css_selector("dl > dd.addr").text)
    price_detail.append(store.find_element_by_css_selector("dd.oil > span:nth-child(1) > em").text)
    price_detail2.append(store.find_element_by_css_selector("dd.oil > span:nth-child(2) > em").text)
print(name, addr,price_detail,price_detail2)

time.sleep(2)

go_next_button = driver.find_element_by_css_selector("#panel > div.panel_content.nano.has-scrollbar > div.scroll_pane.content > div.panel_content_flexible > div.search_result > div > div > a:nth-child(3)")
go_next_button.click()

time.sleep(2)

stores = driver.find_elements_by_css_selector("div.lsnx")

for store in stores:
    # 세부 데이터 수집
    name.append(store.find_element_by_css_selector("dt > a").text)
    addr.append(store.find_element_by_css_selector("dl > dd.addr").text)
    price_detail.append(store.find_element_by_css_selector("dd.oil > span:nth-child(1) > em").text)
    price_detail2.append(store.find_element_by_css_selector("dd.oil > span:nth-child(2) > em").text)
print(name, addr,price_detail,price_detail2)

go_next_button = driver.find_element_by_css_selector("#panel > div.panel_content.nano.has-scrollbar > div.scroll_pane.content > div.panel_content_flexible > div.search_result > div > div > a:nth-child(4)")
go_next_button.click()

time.sleep(2)


stores = driver.find_elements_by_css_selector("div.lsnx")

for store in stores:
    # 세부 데이터 수집
    name.append(store.find_element_by_css_selector("dt > a").text)
    addr.append(store.find_element_by_css_selector("dl > dd.addr").text)
    price_detail.append(store.find_element_by_css_selector("dd.oil > span:nth-child(1) > em").text)
    price_detail2.append(store.find_element_by_css_selector("dd.oil > span:nth-child(2) > em").text)
print(name, addr,price_detail,price_detail2)

data = pd.DataFrame()
data['이름']=list(name)
data['주소']=list(addr)
data['휘발유']=list(price_detail)
data['경유']=list(price_detail2)

data.to_excel("주유소3.xls")
driver.close()

