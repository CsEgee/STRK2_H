import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    # oldal betöltése
    driver.get("http://selenium.oktwebs.training360.com/editable-table.html")
    add_btn = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/button')
    row_count_before = len(driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr'))

    # két új sor hozzáadása és azok meglétének ellenőrzése
    add_btn.click()
    new_row1 = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr[7]/td[1]/input')
    new_row1.send_keys("AirPods" + Keys.TAB + "99" + Keys.TAB + "18" + Keys.TAB + "Electronics")
    add_btn.click()
    new_row2 = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr[8]/td[1]/input')
    new_row2.send_keys("LighningCable" + Keys.TAB + "19" + Keys.TAB + "30" + Keys.TAB + "Electronics")
    row_count_after = len(driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr'))
    assert row_count_before + 2 == row_count_after

    # elektronikai eszközök törlése
    electronics = driver.find_elements(By.XPATH, "//tbody/tr[./td/input[@value='Electronics']]/td[5]/input")

    for item in electronics:
        item.click()
finally:
    driver.close()
