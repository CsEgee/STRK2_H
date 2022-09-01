"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7709_zarovizsga/pw_field.html"

def fill(uname, pw):
    driver.find_element(By.ID, "usrname").send_keys(uname)
    driver.find_element(By.ID, "psw").send_keys(pw)

def pw_check(id):
    if driver.find_element(By.ID, id).get_attribute("class") == "valid":
        return True

tdata_list_uname = ["admin", "admin", "admin", "admin"]
tdata_list_pw = ["aB12aB12", "asdfghjk", "ASDFGHJK", "12345678"]
check_types = ["letter", "capital", "number", "length"]

# TC_001
driver.get(URL)
fill(tdata_list_uname[0], tdata_list_pw[0])
for type in check_types:
    assert pw_check(type)

# TC_002
driver.get(URL)
fill(tdata_list_uname[1], tdata_list_pw[1])
assert pw_check(check_types[0])
assert pw_check(check_types[3])
assert not pw_check(check_types[1])
assert not pw_check(check_types[2])

# TC_003
driver.get(URL)
fill(tdata_list_uname[2], tdata_list_pw[2])
assert pw_check(check_types[1])
assert pw_check(check_types[3])
assert not pw_check(check_types[0])
assert not pw_check(check_types[2])


# TC_004
driver.get(URL)
fill(tdata_list_uname[3], tdata_list_pw[3])
assert pw_check(check_types[2])
assert pw_check(check_types[3])
assert not pw_check(check_types[0])
assert not pw_check(check_types[1])


"""lezárás"""
driver.close()
