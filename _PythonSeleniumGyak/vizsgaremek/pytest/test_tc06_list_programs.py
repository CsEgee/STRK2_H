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


def test_tc06_list_programs(driver, precondition):  # TC06

    # programok listázása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[3]/ul[1]/li[2]/a').click()

    # listázott elemek száma
    found_items = driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset/p/span').text
    found_items_number = int(found_items.strip(' items found, displaying all items.'))
    print(found_items_number)

    # táblázat sorainak száma
    table_rows = driver.find_elements(By.XPATH, '//*[@id="program"]/tbody/tr')
    table_rows_count = len(table_rows)
    print(table_rows_count)

    assert found_items_number == table_rows_count

    # kilépés
    logout(driver)
    time.sleep(1)
