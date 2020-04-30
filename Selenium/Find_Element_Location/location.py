from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://baidu.com")
'''
driver.find_element_by_id("kw").clear()
sleep(2)
driver.find_element_by_id("kw").send_keys("selenium")
sleep(2)
driver.find_element_by_id("su").click()
sleep(2)
'''

'''
search_text=driver.find_element_by_id("kw")
search_text.send_keys("selenium")
sleep(5)
search_text.submit()
'''
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("kw").submit()
sleep(2)
driver.refresh()
driver.quit()