"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome()
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/geometry.html"

def find_and_send(id_inp, tdata):
    driver.find_element(By.ID, id_inp).send_keys(tdata)

def calculating(id_but, id_res):
    driver.find_element(By.ID,id_but).click()
    return driver.find_element(By.ID, id_res).text

# TC_001
def test_geometry_tc1():
    driver.get(URL)
    assert driver.find_element(By.ID, "a").get_attribute("value") == ""
    assert driver.find_element(By.ID, "m").get_attribute("value") == ""
    assert driver.find_element(By.ID, "results").get_attribute("style") == "display: none;"


# TC_002
def test_geometry_tc2():
    driver.get(URL)
    find_and_send("a", 5)
    find_and_send("m", 4)
    assert calculating("submitT", "resultT") == "10.00"
    assert driver.find_element(By.ID, "resultD").text == ""

# TC_003
def test_geometry_tc3():
    driver.get(URL)
    find_and_send("a", 7)
    find_and_send("m", 5)
    assert calculating("submitT", "resultT") == "17.50"
    assert calculating("submitD", "resultD") == "35"


    """lezárás"""
    driver.close()