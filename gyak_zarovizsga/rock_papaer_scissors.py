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
URL = 'http://selenium.oktwebs.training360.com/7904_potzarovizsga/rock_paper_scissors.html'

try:

    # oldal megnyitása
    driver.get(URL)
    time.sleep(1)

    wins = driver.find_element(By.XPATH, '//*[@class="win"]/span')
    ties = driver.find_element(By.XPATH, '//*[@class="tie"]/span')
    losses = driver.find_element(By.XPATH, '//*[@class="loss"]/span')
    total = driver.find_element(By.XPATH, '//*[@class="move"]/span')

    # TC_001: Betöltés utáni állapot tesztelése
    assert wins.text == '0' and ties.text == '0' and losses.text == '0' and total.text == '0'

    # TC_002: Működés megfelelősége:
    driver.find_element(By.ID, 'rock').click()
    result = driver.find_element(By.XPATH, '/html/body/aside/div').get_attribute('class')
    print(result)
    result_value = result.strip('history-item ')
    print(result_value)
    print(driver.find_element(By.XPATH, f'//*[@class="{result_value}"]/span').text)
    assert total.text == '1'

    # TC_003: Frissitsük az oldalt és hajtsunk végre 5 játékot :
    driver.refresh()
    time.sleep(1)

    for i in range(5):
        driver.find_element(By.ID, 'rock').click()
        time.sleep(0.3)

    history_items = driver.find_elements(By.XPATH, '/html/body/aside/div')
    print(len(history_items))
    assert len(history_items) - 2 == 5
    assert driver.find_element(By.XPATH, '//*[@class="move"]/span').text == '5'

finally:
    driver.close()
