from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)
action = ActionChains(driver)
time.sleep(1)

driver.find_element_by_css_selector('#gb_70').click()
time.sleep(3)


action.send_keys('cheysh226@gmail.com').perform()

driver.find_element_by_css_selector('.CwaK9').click()
time.sleep(4)

driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('51477154sh!!')
driver.find_element_by_css_selector('.CwaK9').click()
time.sleep(3)

driver.get('https://mail.google.com/mail/u/0/?ogbl#')
time.sleep(6)

driver.find_element_by_css_selector('.T-I.J-J5-Ji.T-I-KE.L3').click()
time.sleep(5)

send_button = driver.find_element_by_css_selector('.gU.Up')

time.sleep(1)

(
action.pause(2).key_down(Keys.TAB).pause(2).key_down(Keys.TAB).send_keys('제목입니다.').pause(2).key_down(Keys.TAB).pause(2).send_keys('내용입니다.').pause(2).move_to_element(send_button).click().perform()
)

time.sleep(5)
driver.quit()