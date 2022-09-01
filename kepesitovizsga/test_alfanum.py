# importok
import time
import pytest

from selenium import webdriver
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/5201_kepesitovizsga/alfanum.html'

# kitöltő függvény
def fill_form(login_in):
    driver.get(URL)
    driver.find_element(By.ID, 'title').send_keys(login_in)
    time.sleep(1)


def error_check(error_text):
    assert driver.find_element(By.XPATH, '//*[@class="error active"]').text == error_text


def test_tc001():  # TC_001: Helyes kitöltés esete:
    fill_form('abcd1234')
    assert driver.find_element(By.XPATH, '//*[@class="error"]').text == ''


def test_tc002():  # TC_002: Illegális karakterek esete:
    fill_form('teszt233@')
    error_check('Only a-z and 0-9 characters allowed')


def test_tc003():  # TC_003: Túl rövid bemenet esete:
    fill_form('12cd')
    error_check('Login should be at least 8 characters; you entered 4')


def test_004():  # Üres beviteli mező esete (csak kitöltés és törlés esetén jön elő):
    fill_form('12cd')
    time.sleep(0.5)
    for i in range(4):
        driver.find_element(By.ID, 'title').send_keys(Keys.BACKSPACE)
    time.sleep(1)
    error_check('Cannot be empty')

    driver.close()
