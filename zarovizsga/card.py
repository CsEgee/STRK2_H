# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/7709_zarovizsga/card.html'

try:

    # oldal megnyitása
    driver.get(URL)

    # TC_001: A weboldal működése
    pick_a_card = driver.find_element(By.ID, 'submit')
    card_history = []
    for i in range(10):
        pick_a_card.click()
        card_history.append(driver.find_element(By.XPATH, f'//*[@id="deck"]/div[{i+1}]').text)
        last_result = driver.find_element(By.ID, 'lastResult').text
        time.sleep(0.2)
        print(last_result)
        print(card_history)

    assert last_result == card_history[-1]
    time.sleep(1)

    # TC_002: Random működés statisztikai ellenőrzése
    driver.refresh()
    pick_a_card = driver.find_element(By.ID, 'submit')
    card_history40 = []
    for i in range(40):
        pick_a_card.click()
        card_history40.append(driver.find_element(By.XPATH, f'//*[@id="deck"]/div[{i + 1}]').text)
        print(card_history40)

    spades_number = 0
    for i in range(40):
        card = card_history40[i]
        if card.find('♠') > 0:
            spades_number += 1
        else:
            pass

    print(card_history40)
    print(len(card_history40))
    print(spades_number)

    if spades_number in range(9, 12):
        print('A kártyahúzás random algoritmusa megbízható!')
    else:
        print('A kártyahúzás random algoritmusa nem megbízható!')

    assert spades_number in range(9, 12)

finally:
    driver.close()