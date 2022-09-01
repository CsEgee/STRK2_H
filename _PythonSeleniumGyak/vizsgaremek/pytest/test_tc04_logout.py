# importok
import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from common_functions import login, logout


# driver definiálása fixture-rel
@pytest.fixture()
def driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# előfeltétel megvalósítása fixture-rel
@pytest.fixture()
def precondition(driver):
    # bejelentkezés admin oldalra
    login(driver, 'admin', 'admin12')
    time.sleep(1)


def test_tc04_logout(driver, precondition):  # TC04

    # kilépés
    logout(driver)
    time.sleep(1)

    # kilépés ellenőrzése
    assert driver.current_url == 'http://10.211.55.3:8084/login.htm' or 'http://localhost:8084/login.htm'
