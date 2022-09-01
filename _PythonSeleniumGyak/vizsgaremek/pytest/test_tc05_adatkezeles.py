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


# előfeltétel megvalósítása fixture-rel
@pytest.fixture()
def precondition(driver):
    # bejelentkezés admin oldalra
    login(driver, 'admin', 'admin12')
    time.sleep(1)


def test_tc05_adatkezeles(driver, precondition):  # TC05

    # help kikeresése és megnyitása
    driver.find_element(By.XPATH, '//*[@id="login"]/a[2]').click()
    time.sleep(1)

    # váltás az új ablakra
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'http://10.211.55.3:8084/adminHelp.htm' or 'http://localhost:8084/adminHelp.htm'

    # új fül bezárésa és visszatérés a kiinduló oldalra
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    assert driver.current_url == 'http://10.211.55.3:8084/eduardStartPage.htm' or 'http://localhost:8084/eduardStartPage.htm'

    # kilépés
    logout(driver)
    time.sleep(1)

    driver.close()
