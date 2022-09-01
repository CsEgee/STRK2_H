# importok
import time
import csv
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


def test_tc15_multiple_msg_template_upload(driver, precondition):  # TC15

    # üzenet sablonok oldal megnyitása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[2]/ul/li[2]/a').click()

    # jelenlegi sablonok száma
    table_rows = driver.find_elements(By.XPATH, '//*[@id="template"]/tbody/tr')
    table_rows_count = len(table_rows)
    time.sleep(1)

    # sablonok sorozatos felvitele
    input_csv_content = []

    csvfile = open('msg_templ.csv', 'r')
    input_csv = csv.reader(csvfile, delimiter=',')
    next(input_csv)
    for row in input_csv:
        input_csv_content.append(row)
        driver.find_element(By.XPATH, '//*[@id="functions"]/a').click()
        driver.find_element(By.ID, 'template.templateName').send_keys(row[0])
        driver.find_element(By.ID, 'editor').send_keys(row[1])
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="buttons"]/input').click()
        time.sleep(1)

    # felvitel utáni sablonok száma
    table_rows_new = driver.find_elements(By.XPATH, '//*[@id="template"]/tbody/tr')
    table_rows_new_count = len(table_rows_new)

    print(f'felvitel előtti sablonok száma: {table_rows_count}, felvitel utáni sablonok száma: {table_rows_new_count}')

    # hozzáadott elemek ellenőrzése
    assert int(table_rows_count) + 3 == int(table_rows_new_count)

    # felvitt sablonok törlése
    for i in range(3):
        driver.find_element(By.XPATH, f'//table[@id="template"]//tbody//tr//td[contains(text(),"templ{i+1}")]//following-sibling::td[4]//a[1]').click()
        time.sleep(0.5)
        alert = driver.switch_to.alert
        time.sleep(0.5)
        alert.accept()
        time.sleep(0.5)

    logout(driver)
    time.sleep(1)
