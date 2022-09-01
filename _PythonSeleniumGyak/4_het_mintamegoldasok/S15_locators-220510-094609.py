"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://selenium.oktwebs.training360.com/kitchensink.html")

"""elemek kikeresése"""
element_mousehover = driver.find_element(By.ID, "mousehover")
element_showhide = driver.find_element(By.NAME, "show-hide")
element_confirm = driver.find_element(By.XPATH, '//input[@id="confirmbtn"]')
element_td = driver.find_element(By.XPATH, "//tbody/tr[2]/td[1]")
element_option1 = driver.find_element(By.XPATH, '//option[1]')

collection = [element_mousehover, element_showhide, element_confirm, element_td, element_option1]

"""műveletek az elemekkel"""
for i in collection:
    # print(i)
    if i.get_attribute('value'):
        print(f"value: {i.get_attribute('value')}")
    elif i.text:
        print(f"text: {i.text}")
    else:
        print("no text , no value")

"""lezárás"""
time.sleep(1.0)
driver.close()

