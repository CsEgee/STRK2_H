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


URL = 'http://selenium.oktwebs.training360.com/7904_potzarovizsga/stopwatch.html'


def test_tc001(driver):  # TC_001: Alkalmazás alaphelyzetének tesztelése:
    # oldal megnyitása
    driver.get(URL)
    stopwatch_display = driver.find_element(By.XPATH, '//*[@class="stopwatch"]')
    assert stopwatch_display.text == '00: 00: 00'
    time.sleep(1)
    start_btn = driver.find_element(By.ID, 'start')
    start_btn.click()
    time.sleep(1)
    driver.refresh()
    stopwatch_display = driver.find_element(By.XPATH, '//*[@class="stopwatch"]')
    assert stopwatch_display.text == '00: 00: 00'


def test_tc002(driver):  # TC_002: Megállítás x másodpercnél:
    driver.get(URL)
    start_btn = driver.find_element(By.ID, 'start')
    start_btn.click()
    time.sleep(5)
    stop_btn = driver.find_element(By.ID, 'stop')
    stop_btn.click()
    time.sleep(0.5)
    stopwatch_display = driver.find_element(By.XPATH, '//*[@class="stopwatch"]')
    assert '00: 04: 00' < stopwatch_display.text < '00: 06: 00'


def test_t003(driver):  # TC_003: Lapszámláló tesztelése:
    driver.get(URL)
    start_btn = driver.find_element(By.ID, 'start')
    start_btn.click()
    time.sleep(5)
    stop_btn = driver.find_element(By.ID, 'stop')
    stop_btn.click()
    time.sleep(0.5)
    lap_btn = driver.find_element(By.ID, 'lap')
    lap_btn.click()
    time.sleep(1)
    stopwatch_display = driver.find_element(By.XPATH, '//*[@class="stopwatch"]')
    lap_display = driver.find_element(By.XPATH, '//*[@class="results"]/li[1]')
    assert stopwatch_display.text == lap_display.text
    driver.close()
