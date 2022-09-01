# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/7709_zarovizsga/kor_terulete.html'


# kitöltő függfény létrehozása
def calculate_area(radius):
    driver.find_element(By.ID, 'r').send_keys(radius)
    driver.find_element(By.ID, 'submit').click()
    time.sleep(1)


# ellenörző függfény
def assert_area(radius):
    area = (radius ** 2) * 3.14
    assert driver.find_element(By.ID, 'result').text == str(int(area))


try:

    # oldal megnyitása
    driver.get(URL)

    # TC_001: Helyes kitöltés esete:
    radius_in = 10
    calculate_area(radius_in)
    assert_area(radius_in)

    # TC_002: Negatív számmal történő kitöltés esete:
    driver.refresh()
    radius_in = -5
    calculate_area(radius_in)
    alert = driver.switch_to.alert
    time.sleep(0.5)
    assert alert.text == 'A kör sugara nem lehet negatív szám!'
    alert.accept()
    time.sleep(0.5)

    # TC_003: Nem számokkal történő kitöltés esete:
    driver.refresh()
    radius_in = 'abrakadabra'
    calculate_area(radius_in)
    assert driver.find_element(By.ID, 'result').text == 'NaN'

finally:
    driver.close()
