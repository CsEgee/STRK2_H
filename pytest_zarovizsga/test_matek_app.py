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

URL = 'http://selenium.oktwebs.training360.com/7709_zarovizsga/matek_app.html'


# számoló függfény
def matek(driver):
    num1 = driver.find_element(By.ID, 'num1').text
    num2 = driver.find_element(By.ID, 'num2').text
    num3 = driver.find_element(By.ID, 'num3').text
    op1 = driver.find_element(By.ID, 'op1').text
    op2 = driver.find_element(By.ID, 'op2').text
    driver.find_element(By.ID, 'submit').click()
    result_text = driver.find_element(By.ID, 'result').text
    result = eval(f'{int(num1)} {op1} {int(num2)} {op2} {int(num3)}')
    print(result_text)
    print(result)
    assert result_text == str(result)


def test_tc001(driver):  # TC_001: Teszteld le, hogy helyesen jelenik-e meg az applikáció:
    # oldal megnyitása
    driver.get(URL)
    assert driver.find_element(By.ID, 'result').text == ''


def test_tc002(driver):
    # TC_002: Ellenőrizd a Kalkuláció gomb működését:
    driver.get(URL)
    for i in range(3):
        matek(driver)


def test_tc003(driver):
    # TC_003: Az alkalmazás újratöltése és a kalkuláció elvégzése
    driver.get(URL)
    for i in range(10):
        driver.refresh()
        matek(driver)
