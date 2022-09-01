# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

    # oldal megnyitása
    driver.get('http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/bowling-scorecard.html')

    # TC1 betöltéskor minden mező üres
    for i in range(10):
        assert driver.find_element(By.ID, f'frame{i + 1}').get_attribute('value') == None
        assert driver.find_element(By.ID, f'marker{i}').get_attribute('value') == None
    time.sleep(1)
    print('TC1 pass')

    # TC2 11 strike
    for i in range(11):
        driver.find_element(By.XPATH, '//*[@id="buttons"]/button[11]').click()
        time.sleep(0.3)
    time.sleep(1)

    # kapott értékek ellenőrzése
    marker = []
    for i in range(10):
        value = driver.find_element(By.ID, f'marker{i}').text
        marker.append(value)
    # print(marker)
    assert marker == ['10', '20', '40', '60', '80', '100', '120', '140', '160', '200']
    print('TC2 pass')

    # TC3 Lehetetlen gurítások
    driver.refresh()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="buttons"]/button[7]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="buttons"]/button[6]').click()
    time.sleep(1)
    assert driver.find_element(By.ID, 'comments').text == 'Invalid Roll - there are only ten pins!'
    print('TC3 pass')

finally:
    driver.close()
