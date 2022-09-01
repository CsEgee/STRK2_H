# importok
import time
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/7904_potzarovizsga/geometry.html'


def calculate_areas(base_in, height_in, t_calc, d_calc):
    driver.find_element(By.ID, 'a').send_keys(base_in)
    driver.find_element(By.ID, 'm').send_keys(height_in)
    time.sleep(1)
    if t_calc == True:
        driver.find_element(By.ID, 'submitT').click()
    else:
        pass
    if d_calc == True:
        driver.find_element(By.ID, 'submitD').click()
    else:
        pass
    time.sleep(1)

def test_tc001():   # TC_001: Alapállapot tesztelése:
    driver.get(URL)
    t_area = driver.find_element(By.ID, 'resultT')
    d_area = driver.find_element(By.ID, 'resultD')
    assert t_area.text == '' and d_area.text == ''


def test_tc002():  # TC_002: Háromszög területének kiszámítása (alap * magasság / 2)
    driver.refresh()
    base = 5
    height = 4
    calculate_areas(base, height, True, False)
    t_area = driver.find_element(By.ID, 'resultT')
    d_area = driver.find_element(By.ID, 'resultD')
    print(t_area.text, d_area.text)
    print("{:.2f}".format(base * height / 2))
    assert t_area.text == str("{:.2f}".format(base * height / 2)) and d_area.text == ''


def test_tc003():  # TC_003: Háromszög és rombusz területének kiszámítása (alap * magasság / 2, alap * magasság)
    driver.refresh()
    base = 7
    height = 5
    calculate_areas(base, height, True, True)
    t_area = driver.find_element(By.ID, 'resultT')
    d_area = driver.find_element(By.ID, 'resultD')
    print(t_area.text, d_area.text)
    assert t_area.text == str("{:.2f}".format(base * height / 2)) and d_area.text == str(base * height)

    driver.close()
