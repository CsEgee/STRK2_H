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


def test_tc16_delete_msg_template(driver, precondition):  # TC16

    # üzenet sablonok oldal megnyitása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[2]/ul/li[2]/a').click()

    # törlendő sablon létrehozása (Template X)
    driver.find_element(By.XPATH, '//*[@id="functions"]/a').click()
    driver.find_element(By.ID, 'template.templateName').send_keys('Template X')
    driver.find_element(By.ID, 'editor').send_keys('Template text')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="buttons"]/input').click()
    time.sleep(1)

    # jelenlegi sablonok száma
    table_rows = driver.find_elements(By.XPATH, '//*[@id="template"]/tbody/tr')
    table_rows_count = len(table_rows)
    time.sleep(1)

    # sablon törlése (Template X)
    driver.find_element(By.XPATH, '//table[@id="template"]//tbody//tr//td[contains(text(),"Template X")]//following-sibling::td[4]//a[1]').click()
    time.sleep(1)
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    time.sleep(1)

    # törlés utáni sablonok száma
    table_rows_new = driver.find_elements(By.XPATH, '//*[@id="template"]/tbody/tr')
    table_rows_new_count = len(table_rows_new)

    # hozzáadott elem ellenőrzése
    assert int(table_rows_count) - 1 == int(table_rows_new_count)

    logout(driver)
    time.sleep(1)
