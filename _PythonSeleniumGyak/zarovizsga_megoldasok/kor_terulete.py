"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7709_zarovizsga/kor_terulete.html"
driver.get(URL)
r_field = driver.find_element(By.ID, "r")
calc_button = driver.find_element(By.ID, "submit")

pi = 3.14

tdata_list = [10, -5, "abrakadabra"]
exp_result_list = ["314", "A kör sugara nem lehet negatív szám!", "NaN"]

def fill(tdata):
    r_field.clear()
    r_field.send_keys(tdata)
    calc_button.click()
    return driver.find_element(By.ID, "result").text

# TC_001
assert fill(tdata_list[0]) == exp_result_list[0]

# TC_002
r_field.clear()
r_field.send_keys(tdata_list[1])
calc_button.click()
time.sleep(1)
alert_window = driver.switch_to.alert
assert alert_window.text == exp_result_list[1]
alert_window.accept()
time.sleep(1)

# TC_003
assert fill(tdata_list[2]) == exp_result_list[2]

"""lezárás"""
driver.close()

