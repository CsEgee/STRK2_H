"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome()
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/rock_paper_scissors.html"

def button_pushing(id_but):
    driver.find_element(By.ID, id_but).click()

def last_history():
    return driver.find_element(By.XPATH, "//aside/div[1]").get_attribute("class")

# TC_001
def test_rps_tc1():
    driver.get(URL)
    scoreboard_elements = driver.find_elements(By.XPATH, '//*[@class="scoreboard"]/div/span')
    for element in scoreboard_elements:
        assert element.text == "0"
    time.sleep(1)

# TC_002
def test_rps_tc2():
    driver.get(URL)
    button_pushing("rock")
    assert driver.find_element(By.XPATH, "//div[@class='move']/span").text == '1'
    if last_history() == "history-item win":
        assert driver.find_element(By.XPATH, "//div[@class='win']/span").text == '1'
    elif last_history() == "history-item loss":
        assert driver.find_element(By.XPATH, "//div[@class='loss']/span").text == '1'
    else:
        assert driver.find_element(By.XPATH, "//div[@class='tie']/span").text == '1'
    time.sleep(1)

# TC_003
def test_rps_tc3():
    driver.refresh()
    nr_of_games = 5
    for i in range(nr_of_games):
        button_pushing("paper")
    assert driver.find_element(By.XPATH, "//div[@class='move']/span").text == str(nr_of_games)
    assert len(driver.find_elements(By.XPATH, "//aside/div[starts-with(@class,'history')]")) == nr_of_games
    time.sleep(1)

    """lezárás"""
    driver.close()