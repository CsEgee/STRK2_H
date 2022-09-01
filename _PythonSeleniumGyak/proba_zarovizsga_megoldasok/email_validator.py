"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/email_validator.html"

"""email kitöltés függvénybe szervezve"""
def email_fill(tdata):
    driver.find_element(By.ID, "email").send_keys(tdata)
    driver.find_element(By.ID, "submit").click()

"""hibaüzenet szövegének függvénye"""
def error_message():
    return driver.find_element(By.CLASS_NAME, 'validation-error').text

# TC1
driver.get(URL)
tdata1 = "teszt@elek.hu"
email_fill(tdata1)
assert len(driver.find_elements(By.CLASS_NAME, 'validation-error')) == 0
time.sleep(1)

# TC2
driver.get(URL)
tdata2 = "teszt@"
exp2 = 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'
email_fill(tdata2)
assert error_message() == exp2
time.sleep(1)

# TC3
driver.get(URL)
tdata3 = ""
exp3 = 'Kérjük, töltse ki ezt a mezőt.'
email_fill(tdata3)
assert error_message() == exp3
time.sleep(1)

"""lezárás"""
driver.close()

