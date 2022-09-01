# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/5201_kepesitovizsga/twitter.html'


def test_tc001():  # TC_001: Új tweet felvétele:
    driver.get(URL)
    new_tweet_text = 'New twitter post arrived'
    driver.find_element(By.XPATH, '//*[@class="flex-1"]/textarea').send_keys('New twitter post arrived')
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/button').click()
    time.sleep(0.5)
    new_tweet = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/ul/div[1]/li/div/div[2]/div[2]/p')
    assert new_tweet.text == new_tweet_text


def test_tc002():  # TC_002: Követés beállítása:
    driver.get(URL)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/ul[1]/li[3]/div/div[2]/div[2]/button').click()
    time.sleep(1)
    initials = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/ul[2]/li[4]/div/div[1]/div/span')
    assert initials.text == 'CN'


def test_tc003():  # TC_003: Követés megszüntetése:
    driver.get(URL)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/ul[2]/li[2]/div/div[2]/div[2]/button').click()
    time.sleep(1)
    initials = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/ul[1]/li[5]/div/div[1]/div/span')
    assert initials.text == 'PN'

    driver.close()

