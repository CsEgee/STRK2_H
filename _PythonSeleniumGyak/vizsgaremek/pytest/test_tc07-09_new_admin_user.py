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

    # felhasználók oldal megnyitása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[3]/ul[1]/li[1]/a').click()


def new_user(driver, username, pwd, f_name, g_name, email):
    driver.find_element(By.XPATH, '//*[@id="functions"]/a').click()
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[1]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[2]').send_keys(pwd)
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[3]').send_keys(pwd)
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[4]').send_keys(f_name)
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[5]').send_keys(g_name)
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[6]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="user.role"]/option[4]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="buttons"]/input').click()
    time.sleep(1)


def test_tc07_new_admin_user(driver, precondition):  # TC07

    # jelenlegi felhasználók száma
    table_rows = driver.find_elements(By.XPATH, '//*[@id="user"]/tbody/tr')
    table_rows_count = len(table_rows)
    time.sleep(1)

    # új admin felhasználó hozzáadása
    new_user(driver, 'admintest', 'admintest12', 'Teszt', 'Elekina', 'teszt.elekina@mail.com')

    # firssített felhasználók száma
    table_rows_new = driver.find_elements(By.XPATH, '//*[@id="user"]/tbody/tr')
    table_rows_new_count = len(table_rows_new)

    # hozzáadott elem ellenőrzése
    assert int(table_rows_count) + 1 == int(table_rows_new_count)

    # hozzáadott felhasználó működésének ellenőrzése
    logout(driver)
    time.sleep(1)
    login(driver, 'admintest', 'admintest12')
    time.sleep(1)

    # belépett felhasználó ellenőrzése
    user_logged_in = driver.find_element(By.XPATH, '//*[@id="login"]').text
    assert user_logged_in == 'Logged in: admintest::Administrator | Log out | Help'

    # környezet visszaállítása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[3]/ul[1]/li[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//table[@id="user"]//tbody//tr//td[contains(text(),"admintest")]//following-sibling::td[3]//a[1]').click()
    time.sleep(1)
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    logout(driver)
    time.sleep(1)


def test_tc08_new_existing_admin_user(driver, precondition):  # TC08

    # létező felhasználói név kikeresése
    existing_username = driver.find_element(By.XPATH, '//*[@id="user"]/tbody/tr[1]/td[1]').text

    # új admin felhasználó hozzáadása
    new_user(driver, existing_username, 'admintest12', 'Teszt', 'Elekina', 'teszt.elekina@mail.com')
    time.sleep(1)

    # hibaüzenet ellenőrzése
    warning_text = driver.find_element(By.XPATH, '//*[@id="error"][1]').text
    assert warning_text == 'Username must be unique throughout the system!'

    logout(driver)


def test_tc09_new_empty_fields_user(driver, precondition):  # TC09

    # üres űrlap mentése
    new_user(driver, '', '', '', '', '')
    time.sleep(1)

    # hibaüzenetek ellenőrzése
    assert driver.find_element(By.XPATH, '//*[@id="error"][1]').text == 'Username required'
    assert driver.find_element(By.XPATH, '//*[@id="error"][2]').text == 'Password must be given'
    assert driver.find_element(By.XPATH, '//*[@id="error"][3]').text == 'Family name required'
    assert driver.find_element(By.XPATH, '//*[@id="error"][4]').text == 'Given name required'

    logout(driver)
