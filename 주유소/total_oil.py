from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://map.naver.com/v5/api/search?caller=pcweb&query=%EC%A3%BC%EC%9C%A0%EC%86%8C&type=place&searchCoord=128.3562755584717;36.07865577441875&page=1&displayCount=150&isPlaceRecommendationReplace=true&lang=ko")

stores = driver.find_elements_by_name("rank")
name=[]
for store in stores:
    name.append(store.find_element_by_name("name").text)
print(name)
driver.close()