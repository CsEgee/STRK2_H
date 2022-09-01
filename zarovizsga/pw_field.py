# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/7709_zarovizsga/pw_field.html'

# kitöltő függfény
def fill_pwd(user, pwd):
    driver.find_element(By.ID, 'usrname').send_keys(user)
    driver.find_element(By.ID, 'psw').send_keys(pwd)


# ellenörző függfény
def assert_pwd(letter_v, capital_v, number_v, length_v):
    assert driver.find_element(By.ID, 'letter').get_attribute('class') == letter_v
    assert driver.find_element(By.ID, 'capital').get_attribute('class') == capital_v
    assert driver.find_element(By.ID, 'number').get_attribute('class') == number_v
    assert driver.find_element(By.ID, 'length').get_attribute('class') == length_v


try:

    # oldal megnyitása
    driver.get(URL)

    # TC_001: Helyes kitöltés esete:
    user_in = 'admin'
    pwd_in = 'aB12aB12'
    fill_pwd(user_in, pwd_in)
    time.sleep(1)
    assert_pwd('valid', 'valid', 'valid', 'valid')

    # TC_002: Csak kisbetűk a jelszóban:
    driver.refresh()
    user_in = 'admin'
    pwd_in = 'asdfghjk'
    fill_pwd(user_in, pwd_in)
    time.sleep(1)
    assert_pwd('valid', 'invalid', 'invalid', 'valid')

    # TC_003: Csak nagybetűk a jelszóban:
    driver.refresh()
    user_in = 'admin'
    pwd_in = 'ASDFGHJK'
    fill_pwd(user_in, pwd_in)
    time.sleep(1)
    assert_pwd('invalid', 'valid', 'invalid', 'valid')

    # TC_004: Csak számok a jelszóban:
    driver.refresh()
    user_in = 'admin'
    pwd_in = '12345678'
    fill_pwd(user_in, pwd_in)
    time.sleep(1)
    assert_pwd('invalid', 'invalid', 'valid', 'valid')


finally:
    driver.close()