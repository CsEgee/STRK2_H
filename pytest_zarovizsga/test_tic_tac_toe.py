# importok
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/7709_zarovizsga/tic_tac_toe.html'

try:

    # oldal megnyitása
    driver.get(URL)

    # elemek kikeresése
    board_size = driver.find_element(By.ID, 'board-size')
    win_size = driver.find_element(By.ID, 'win-size')
    start_game_btn = driver.find_element(By.XPATH, '/html/body/div[1]/button')

    # TC_001: Megjelenés és beállítások:
    tile_number = int(board_size.get_attribute('value'))**2
    print(board_size.get_attribute('value'))
    print(tile_number)

    # alaphelyzet ellenőrzése
    for i in range(tile_number):
        assert driver.find_element(By.XPATH, f'//*[@id="game-board"]/div[{i+1}]').text == '?'

    # táblaméret és nyerőszám ellenőrzése
    # driver.find_element(By.ID, 'board-size').clear()
    # driver.find_element(By.ID, 'board-size').send_keys(random.randrange(1, 50))
    # driver.find_element(By.ID, 'win-size').clear()
    # driver.find_element(By.ID, 'win-size').send_keys(random.randrange(1, 50))
    # time.sleep(1)
    # start_game_btn.click()

    if int(win_size.get_attribute('value')) > int(board_size.get_attribute('value')):
        alert = driver.switch_to.alert
        assert alert.text == 'Make your params consistant !'
        alert.accept()
    else:
        pass

    # TC_002: Játék működésének tesztelése:
    print(int(win_size.get_attribute('value')))
    for i in range(int(win_size.get_attribute('value'))):
        driver.find_element(By.XPATH, f'//*[@id="game-board"]/div[{i + 1}]').click()
    time.sleep(2)

finally:
    driver.close()