# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from common_functions import login, logout

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# TC11
# előfeltétel megvalósítása (bejelentkezés admin oldalra)
try:
    login(driver, 'admin', 'admin12')
    time.sleep(1)

    # hallgatók lista betöltése
    driver.find_element(By.XPATH, '/html/body/div[1]/h1/a').click()

    # listázott hallgatók száma
    found_students = driver.find_element(By.XPATH, '//*[@id="functions"]/span').text
    number_of_students = int(found_students.strip('Number of students :: '))

    # lista bejárása és sorok számolása
    table_rows_sum = 0
    while True:
        time.sleep(1)
        # sorok számolása oldalanként
        table_rows = driver.find_elements(By.XPATH, '//*[@id="student"]/tbody/tr')
        table_rows_count = len(table_rows)
        table_rows_sum = table_rows_sum + table_rows_count

        # lépés következő oldalra
        next = driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset/p/a[5]')

        if not next.get_attribute('href'):
            break
        else:
            next.click()

    # sorok számának összehasonlítása a listázott hallgatók számával
    assert table_rows_sum == number_of_students
    print(f'táblázat sorainak száma: {table_rows_sum}, diákok száma: {number_of_students}')

    # kilépés
    logout(driver)
    time.sleep(1)

finally:
    driver.close()