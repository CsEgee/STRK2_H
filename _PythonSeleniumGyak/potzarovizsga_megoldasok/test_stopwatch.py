"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome()
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/stopwatch.html"

def button_pushing(id_but):
    driver.find_element(By.ID, id_but).click()

def check_watch():
    return driver.find_element(By.CLASS_NAME, "stopwatch").text

# TC_001
def test_stopwatch_tc1():
    driver.get(URL)
    assert check_watch() == "00: 00: 00"
    button_pushing("start")
    time.sleep(0.2)
    driver.get(URL)
    assert check_watch() == "00: 00: 00"
    time.sleep(1)

# TC_002
def test_stopwatch_tc2():
    driver.get(URL)
    button_pushing("start")
    time.sleep(5)
    button_pushing("stop")
    assert "00: 04: 00" <= check_watch() <= "00: 06: 00"
    print("TC002 print result: ", driver.find_element(By.CLASS_NAME, "stopwatch").text)
    time.sleep(1)

# TC_003
def test_stopwatch_tc3():
    driver.get(URL)
    button_pushing("start")
    time.sleep(5)
    button_pushing("stop")
    button_pushing("lap")
    assert check_watch() == driver.find_element(By.XPATH, "//ul/li").text
    time.sleep(1)

    """lezárás"""
    driver.close()