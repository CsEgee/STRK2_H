# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = 'http://selenium.oktwebs.training360.com/5201_kepesitovizsga/penzfeldobas.html'


def test_tc001():  # TC_001: Az utolsó eredmény és a pénzfeldobások historyjának ellenőrzése:
    driver.get(URL)
    flip_btn = driver.find_element(By.ID, 'submit')
    coin_history = []
    for i in range(10):
        flip_btn.click()
        coin_history.append(driver.find_element(By.XPATH, f'//*[@id="results"]/li[{i+1}]').text)
        last_result = driver.find_element(By.ID, 'lastResult').text
        time.sleep(0.2)
        print(last_result)
        print(coin_history)

    assert last_result == coin_history[-1]


def test_tc002():  # TC_002: A random működés ellenőrzése:
    try:
        driver.get(URL)
        flip_btn = driver.find_element(By.ID, 'submit')

        def coin_flip100():
            coin_history100 = []
            for i in range(100):
                flip_btn.click()
                coin_history100.append(driver.find_element(By.XPATH, f'//*[@id="results"]/li[{i+1}]').text)
                # print(coin_history100)

            heads_counter = 0
            for i in range(100):
                coin = coin_history100[i]
                # print(coin)
                if coin.find('fej'):
                    heads_counter += 1
                    # print(heads_counter)
                else:
                    pass
            # print(heads_counter)
            return heads_counter

        print(coin_flip100())

        if coin_flip100() in range(44, 55):
            print('A pénzfeldobás random algoritmusa megbízható!')
        else:
            print('A pénzfeldobás random algoritmusa nem megbízható!')

        assert coin_flip100() in range(44, 55)

        # heads = []
        # for k in range(3):
        #     heads_number = coin_flip100()
        #     heads.append(heads_number)
        #
        # average_heads = sum(heads) / len(heads)
        # print(heads)
        # print(f'a fejek átlaga: {average_heads}: ')

    finally:
        driver.close()
