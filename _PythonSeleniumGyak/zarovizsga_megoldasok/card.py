"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7709_zarovizsga/card.html"

def find_id(id):
    return driver.find_element(By.ID, id)

def draw_process(draw_nr):
    for i in range(draw_nr):
        find_id("submit").click()

# TC_001
driver.get(URL)
nr_of_draw_tc1 = 10
draw_process(nr_of_draw_tc1)

assert find_id("lastResult").text == driver.find_element(By.XPATH, f"//*[@id='deck']/div[{nr_of_draw_tc1}]").text
time.sleep(2)

# TC_002
driver.get(URL)
nr_of_draw_tc2 = 40
draw_process(nr_of_draw_tc2)

cards = driver.find_elements(By.CLASS_NAME, "card")
check_nr = 0
for card in cards:
    if "♠" in card.text:
        check_nr += 1
print(check_nr)
assert check_nr<=11 and check_nr>=9


"""lezárás"""
driver.close()