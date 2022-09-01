"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome()
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/toggle.html"

# TC_001
def test_toggle_tc1():
    driver.get(URL)
    assert driver.find_element(By.XPATH, "//div[@class='container']/h1").text == "Slide Down Toggle"
    assert driver.find_element(By.TAG_NAME, "label").is_enabled()
    assert driver.find_element(By.TAG_NAME, "label").is_displayed()
    time.sleep(1)

# TC_002
def test_toggle_tc2():
    driver.get(URL)
    driver.find_element(By.TAG_NAME, "label").click()
    time.sleep(0.5)
    assert driver.find_element(By.XPATH, "//div[@class='message']/h1").text == "This is the hidden message."
    assert driver.find_element(By.XPATH, "//div[@class='message']/h1").is_displayed()
    time.sleep(1)
    driver.find_element(By.TAG_NAME, "label").click()
    time.sleep(0.5)
    assert driver.find_element(By.XPATH, "//div[@class='container']/h1").text == "Slide Down Toggle"
    assert driver.find_element(By.TAG_NAME, "label").is_enabled()
    assert driver.find_element(By.TAG_NAME, "label").is_displayed()


    """lezárás"""
    driver.close()