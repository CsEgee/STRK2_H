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


URL = 'http://selenium.oktwebs.training360.com/7709_zarovizsga/kor_terulete.html'


# kitöltő függfény létrehozása
def calculate_area(driver, radius):
    driver.find_element(By.ID, 'r').send_keys(radius)
    driver.find_element(By.ID, 'submit').click()
    time.sleep(1)


# ellenörző függfény
def assert_area(driver, radius):
    area = (radius ** 2) * 3.14
    assert driver.find_element(By.ID, 'result').text == str(int(area))


def test_tc001(driver):  # TC_001: Helyes kitöltés esete:
    # oldal megnyitása
    driver.get(URL)

    radius_in = 10
    calculate_area(driver, radius_in)
    assert_area(driver, radius_in)


def test_tc002(driver):  # TC_002: Negatív számmal történő kitöltés esete:
    driver.get(URL)
    radius_in = -5
    calculate_area(driver, radius_in)
    alert = driver.switch_to.alert
    time.sleep(0.5)
    assert alert.text == 'A kör sugara nem lehet negatív szám!'
    alert.accept()
    time.sleep(0.5)


def test_tc003(driver):  # TC_003: Nem számokkal történő kitöltés esete:
    driver.get(URL)
    radius_in = 'abrakadabra'
    calculate_area(driver, radius_in)
    assert driver.find_element(By.ID, 'result').text == 'NaN'
