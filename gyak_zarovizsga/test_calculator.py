# importok
import time
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


# driver definiálása fixture-rel
@pytest.fixture()
def driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = 'http://selenium.oktwebs.training360.com/7904_potzarovizsga/calculator.html'


def type_numbers(driver, number):
    actions = ActionChains(driver)
    actions.send_keys(number)
    actions.perform()
    time.sleep(0.5)


def test_calculator(driver):
    # oldal megnyitása
    driver.get(URL)

    # szükséges elemek (gombok) kikeresése, változóba mentése
    key_add = driver.find_element(By.XPATH, '//*[@class="calculator-key key-add"]')
    key_equals = driver.find_element(By.XPATH, '//*[@class="calculator-key key-equals"]')
    key_multiply = driver.find_element(By.XPATH, '//*[@class="calculator-key key-multiply"]')
    key_percent = driver.find_element(By.XPATH, '//*[@class="calculator-key key-percent"]')

    # Két árucikkünk van (1-1 darab). Az egyik árucikk nettó értéke 1000 Ft, a másiké nettó 3000 Ft.
    # Számítsuk ki a két árucikk nettó összértéket a kalkulátor segítségével!
    type_numbers(driver, 1000)
    key_add.click()
    type_numbers(driver, 3000)
    key_equals.click()
    time.sleep(1)
    result_text = driver.find_element(By.XPATH, '//*[@class="auto-scaling-text"]').text
    print(result_text)
    assert result_text == '4 000'

    # Számítsuk ki a két árucikk áfa (27%) összegét.
    key_multiply.click()
    type_numbers(driver, 27)
    key_percent.click()
    key_equals.click()

    # Ellenőrizzük a kiszámított áfa összeget, a várt összeg 1080 Ft.
    result_text = driver.find_element(By.XPATH, '//*[@class="auto-scaling-text"]').text
    print(result_text)
    assert result_text == '1 080'

    # Számítsuk ki a bruttó értéket, azaz adjuk hozzá a kiszámított nettó összértékhez a kiszámított áfa összeget!
    key_add.click()
    type_numbers(driver, 4000)
    key_equals.click()

    # Ellenőrizzük a kapott bruttó értéket, a várt érték 5080 Ft.
    result_text = driver.find_element(By.XPATH, '//*[@class="auto-scaling-text"]').text
    print(result_text)
    assert result_text == '5 080'
