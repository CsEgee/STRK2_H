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


URL = 'http://selenium.oktwebs.training360.com/7904_potzarovizsga/toggle.html'


def test_tc001(driver):  # TC_001: Alap megjelenés tesztelése:
    driver.get(URL)
    assert driver.find_element(By.XPATH, '//*[@class="container"]/h1').text == 'Slide Down Toggle'
    assert driver.find_element(By.ID, 'toggle').is_selected() == False


def test_tc002(driver):  # TC_002: A toggle működtetése:
    driver.get(URL)
    driver.find_element(By.XPATH, '/html/body/label').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@class="message"]/h1').text == 'This is the hidden message.'
    assert driver.find_element(By.ID, 'toggle').is_selected() == True
    driver.find_element(By.XPATH, '/html/body/label').click()
    assert driver.find_element(By.XPATH, '//*[@class="container"]/h1').text == 'Slide Down Toggle'
    assert driver.find_element(By.ID, 'toggle').is_selected() == False
