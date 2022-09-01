"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7709_zarovizsga/tic_tac_toe.html"

# TC_001
driver.get(URL)
tiles = driver.find_elements(By.CLASS_NAME, "tile")
for tile in tiles:
    assert tile.text == "?"

board_size = int(driver.find_element(By.ID, "board-size").get_attribute("value"))
win_size = driver.find_element(By.ID, "win-size")
new_win_size = 7
if board_size < new_win_size:
    win_size.send_keys(new_win_size)
    start_game_button = driver.find_element(By.TAG_NAME, "button")
    start_game_button.click()
    alert_window = driver.switch_to.alert
    assert alert_window.text == "Make your params consistant !"
    alert_window.accept()

# TC_002
driver.get(URL)
tiles = driver.find_elements(By.CLASS_NAME, "tile")
for tile in tiles[0::6]:
    tile.click()
for tile in tiles[1::6]:
    tile.click()
for tile in tiles[2::6]:
    tile.click()
for tile in tiles[3:4:1]:
    tile.click()
time.sleep(1)
alert_window = driver.switch_to.alert
assert "Game Over" in alert_window.text
assert alert_window.text.startswith("Game Over")
alert_window.accept()
time.sleep(1)

"""lezárás"""
driver.close()