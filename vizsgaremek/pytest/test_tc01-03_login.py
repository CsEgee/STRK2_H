# importok
import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from common_functions import login, logout


# driver definiálása fixture-rel
@pytest.fixture()
def driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_tc01_login(driver):  # TC01

    # login oldal betöltése és sikeres bejelentkezés admin / admin12 kredenciálissal
    login(driver, 'admin', 'admin12')
    time.sleep(1)

    # várt URL ellenőrzése
    assert driver.current_url == 'http://10.211.55.3:8084/eduardStartPage.htm' or 'http://localhost:8084/eduardStartPage.htm'

    # beléptetett felhasználó ellenőrzése
    user_logged_in = driver.find_element(By.XPATH, '//*[@id="login"]').text
    assert user_logged_in == 'Logged in: admin::Administrator | Log out | Help'

    # kilépés
    logout(driver)
    time.sleep(1)


def test_tc02_wrong_pwd_login(driver):  # TC02

    # login oldal betöltése és hibás bejelentkezés admin / admin kredenciálissal
    login(driver, 'admin', 'admin')
    time.sleep(1)

    # hibaüzenet meglétének ellenőrzése
    assert driver.find_element(By.XPATH, '//*[@id="loginData"]/fieldset[1]/div').text == 'Login failed!'


def test_tc03_wrong_username_login(driver):  # TC03

    # login oldal betöltése és hibás bejelentkezés admin / admin kredenciálissal
    login(driver, 'admin12', 'admin12')
    time.sleep(1)

    # hibaüzenet meglétének ellenőrzése
    assert driver.find_element(By.XPATH, '//*[@id="loginData"]/fieldset[1]/div').text == 'Login failed!'

