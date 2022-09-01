# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/5201_kepesitovizsga/input-pattern.html'


# kitöltő függvény:
def fill_form(tr_id, text_in):
    input_field = driver.find_element(By.XPATH, f'//*[@id="{tr_id}"]/td[2]/input')
    input_field.send_keys(text_in)
    time.sleep(0.5)


def assert_field(tr_id, text_out):
    assert driver.find_element(By.XPATH, f'//*[@id="{tr_id}"]/td[2]/input').get_attribute('value') == text_out


def test_tc001():  # TC_001: ALPHA ONLY esetén
    driver.get(URL)
    fill_form(1, 'ab1ef2ij3op4uv5')
    assert_field(1, 'abefijopuv')


def test_tc002():  # TC_002: NUMBER ONLY esetén
    driver.get(URL)
    fill_form(2, 'ab1ef2ij3op4uv5')
    assert_field(2, '12345')


def test_tc003():  # TC_003: ALPHANUMERIC ONLY esetén
    driver.get(URL)
    fill_form(3, 'ab1ef2ij3op4uv5')
    assert_field(3, 'ab1ef2ij3op4uv5')


def test_tc004():  # TC_004: VOWEL ONLY esetén
    driver.get(URL)
    fill_form(5, 'ab1ef2ij3op4uv5')
    assert_field(5, 'aeiou')

    driver.close()

