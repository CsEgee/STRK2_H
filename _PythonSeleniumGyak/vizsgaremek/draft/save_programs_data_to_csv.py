# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from common_functions import login, logout

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# TC10
# előfeltétel megvalósítása (bejelentkezés admin oldalra)
try:
    login(driver, 'admin', 'admin12')
    time.sleep(1)

    # programok oldal megnyitása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[3]/ul[1]/li[2]/a').click()
    time.sleep(1)

    # sorok első két oszlopának gyűjtése listába
    rowcount = len(driver.find_elements(By.XPATH, '//table/tbody/tr'))
    columncount = 2

    rows = []
    for i in range(rowcount):
        columns = []
        for j in range(columncount):
            value = driver.find_element(By.XPATH, f'//table/tbody/tr[{i + 1}]/td[{j + 1}]').text
            columns.append(value)
        rows.append(columns)
    print(rows)
    print(len(rows))

    # listázott elemek megjelenített száma
    found_items = driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset/p/span').text
    found_items_number = int(found_items.strip(' items found, displaying all items.'))

    # gyűjtött sorok ellenőrzése
    assert len(rows) == found_items_number

    # gyűjtött sorok kiírása CSV fájlba
    file = open('programs.csv', "w")
    file.write('ABBREVIATION,NAME')
    file.write("\n")
    for row in rows:
        str = ",".join(row)
        file.write(str)
        file.write("\n")
    file.close()

    # kilépés
    logout(driver)
    time.sleep(1)

finally:
    driver.close()
