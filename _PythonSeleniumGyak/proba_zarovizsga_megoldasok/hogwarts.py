"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/hogwarts.html"


"""beviteli mezők kitöltése függvénybe szervezve"""
def fill_form(pas, dep_d, dep_t):
    driver.find_element(By.ID, "passenger").send_keys(pas)
    driver.find_element(By.ID, "departure-date").send_keys(dep_d)
    driver.find_element(By.ID, "departure-time").send_keys(dep_t)
    driver.find_element(By.ID, "issue-ticket").click()

"""ellenőrzendő mező szövegének függvénybe szervezése"""
def check(id):
    return driver.find_element(By.ID, id).text

# TC1
name1 = "Harry Potter"
dep_d1 = "2022\t-09-01"
dep_t1 = "10:00"
driver.get(URL)
fill_form(name1, dep_d1, dep_t1)
assert check("passenger-name") == name1.upper()
assert check("departure-date-text") == "2022-09-01"
assert check("departure-time-text") == "10:00AM"
assert check("side-detparture-date") == "2022-09-01"
assert check("side-departure-time") == "10:00AM"
time.sleep(1)

# TC2
name2 = ""
dep_d2 = "2022\t-09-01"
dep_t2 = "10:00"
driver.get(URL)
fill_form(name2, dep_d2, dep_t2)
assert check("passenger-name") == name2.upper()
assert check("departure-date-text") == "2022-09-01"
assert check("departure-time-text") == "10:00AM"
assert check("side-detparture-date") == "2022-09-01"
assert check("side-departure-time") == "10:00AM"
time.sleep(1)
#
# # TC3
name3 = "Harry Potter"
dep_d3 = "2022\t-\t-\t"
dep_t3 = "10:00"
driver.get(URL)
fill_form(name3, dep_d3, dep_t3)
assert check("passenger-name") == "XXXXXXXX XXXXXXXX"
assert check("departure-date-text") == "XX YYY ZZZZ"
assert check("departure-time-text") == "XX:YYZZ"
assert check("side-detparture-date") == "XX YYY ZZZZ"
assert check("side-departure-time") == "XX:YYZZ"
time.sleep(1)


"""lezárás"""
driver.close()