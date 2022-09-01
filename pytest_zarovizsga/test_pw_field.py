# importok
import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver definiálása fixture-rel
@pytest.fixture()
def driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = 'http://selenium.oktwebs.training360.com/7709_zarovizsga/pw_field.html'

# kitöltő függfény
def fill_pwd(driver, user, pwd):
    driver.find_element(By.ID, 'usrname').send_keys(user)
    driver.find_element(By.ID, 'psw').send_keys(pwd)


# ellenörző függfény
def assert_pwd(driver, letter_v, capital_v, number_v, length_v):
    assert driver.find_element(By.ID, 'letter').get_attribute('class') == letter_v
    assert driver.find_element(By.ID, 'capital').get_attribute('class') == capital_v
    assert driver.find_element(By.ID, 'number').get_attribute('class') == number_v
    assert driver.find_element(By.ID, 'length').get_attribute('class') == length_v


def test_tc001(driver):  # TC_001: Helyes kitöltés esete:
    # oldal megnyitása
    driver.get(URL)

    user_in = 'admin'
    pwd_in = 'aB12aB12'
    fill_pwd(driver, user_in, pwd_in)
    time.sleep(1)
    assert_pwd(driver, 'valid', 'valid', 'valid', 'valid')


def test_tc002(driver):  # TC_002: Csak kisbetűk a jelszóban:
    driver.get(URL)
    user_in = 'admin'
    pwd_in = 'asdfghjk'
    fill_pwd(driver, user_in, pwd_in)
    time.sleep(1)
    assert_pwd(driver, 'valid', 'invalid', 'invalid', 'valid')


def test_tc003(driver):  # TC_003: Csak nagybetűk a jelszóban:
    driver.get(URL)
    user_in = 'admin'
    pwd_in = 'ASDFGHJK'
    fill_pwd(driver, user_in, pwd_in)
    time.sleep(1)
    assert_pwd(driver, 'invalid', 'valid', 'invalid', 'valid')


def test_tc004(driver):  # TC_004: Csak számok a jelszóban:
    driver.get(URL)
    user_in = 'admin'
    pwd_in = '12345678'
    fill_pwd(driver, user_in, pwd_in)
    time.sleep(1)
    assert_pwd(driver, 'invalid', 'invalid', 'valid', 'valid')
