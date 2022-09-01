# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/5201_kepesitovizsga/pitagorasz.html'


# kitöltő függvény:
def fill_form(a_in, b_in):
    driver.find_element(By.ID, 'a').send_keys(a_in)
    driver.find_element(By.ID, 'b').send_keys(b_in)
    time.sleep(0.5)
    driver.find_element(By.ID, 'submit').click()
    time.sleep(1)


def assert_result(result_out):
    assert driver.find_element(By.ID, 'result').text == result_out


def test_tc001():  # TC_001: Helyes kitöltés esete:
    driver.get(URL)
    fill_form(3, 4)
    assert_result("{:.2f}".format(5))


def test_tc002():  # TC_002: Illegális karakterek esete:
    driver.get(URL)
    fill_form('a', 4)
    assert_result('NaN')


def test_tc003():  # TC_003: Illegális karakterek esete:
    driver.get(URL)
    fill_form(3, 'b')
    assert_result('NaN')


def test_tc004():  # TC_004: Üres beviteli mezők esete:
    driver.get(URL)
    fill_form('', '')
    assert_result('NaN')

    driver.close()
