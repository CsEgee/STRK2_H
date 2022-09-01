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

    # programok oldal megnyitása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[3]/ul[1]/li[2]/a').click()


def test_tc11_new_program(driver, precondition):  # TC10

    # jelenlegi programok száma
    table_rows = driver.find_elements(By.XPATH, '//*[@id="program"]/tbody/tr')
    table_rows_count = len(table_rows)
    time.sleep(1)

    # új program hozzáadása
    driver.find_element(By.XPATH, '//*[@id="functions"]/a').click()
    driver.find_element(By.ID, 'program.programName').send_keys('Master Medicine Course')
    driver.find_element(By.ID, 'program.programCode').send_keys('MMC')
    driver.find_element(By.XPATH, '//*[@id="program.faculty"]/option[3]').click()
    driver.find_element(By.XPATH, '//*[@id="program.programLevel"]/option[4]').click()
    study_duration = driver.find_element(By.ID, 'program.studyDuration')
    study_duration.clear()
    study_duration.send_keys('4')
    reservation_fee = driver.find_element(By.ID, 'program.seatReservationFee')
    reservation_fee.clear()
    reservation_fee.send_keys('2000')
    tuition_fee = driver.find_element(By.ID, 'program.tuitionFee')
    tuition_fee.clear()
    tuition_fee.send_keys('24000')
    # driver.find_element(By.XPATH, 'program.listOnSelfApplication1').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="buttons"]/input').click()
    time.sleep(1)

    # firssített programok száma
    table_rows_new = driver.find_elements(By.XPATH, '//*[@id="program"]/tbody/tr')
    table_rows_new_count = len(table_rows_new)

    # hozzáadott elem ellenőrzése
    assert int(table_rows_count) + 1 == int(table_rows_new_count)

    # környezet visszaállítása
    driver.find_element(By.XPATH, '//table[@id="program"]//tbody//tr//td[contains(text(),"MMC")]//following-sibling::td[3]//a[1]').click()
    time.sleep(1)
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    logout(driver)
    time.sleep(1)


def test_tc12_new_empty_program(driver, precondition):  # TC11

    # új program hozzáadása
    driver.find_element(By.XPATH, '//*[@id="functions"]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="buttons"]/input').click()
    time.sleep(1)

    # hibaüzenetek ellenőrzése
    assert driver.find_element(By.XPATH, '//*[@id="error"][1]').text == 'Program name is required.'
    assert driver.find_element(By.XPATH, '//*[@id="error"][2]').text == 'Code is required.'

    logout(driver)