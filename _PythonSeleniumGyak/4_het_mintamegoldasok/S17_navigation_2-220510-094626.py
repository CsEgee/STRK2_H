#importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

#driver létrehozása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#elemek kikeresése
try:
    driver.get("http://selenium.oktwebs.training360.com/general.html")
    links = driver.find_elements(By.XPATH, '//a')

    for i in links:
        if i.text == '#':
            links.remove(i)

#műveletek az elemekkel
    for i in range(len(links)):
        link = driver.find_elements(By.XPATH, '//a')[i]
        val = link.get_attribute('href')
        if link.get_attribute('target'):
            win = driver.window_handles[0]
            link.click()
            driver.switch_to.window(driver.window_handles[1])
            if driver.current_url == val:
                print("Good URL")
                print(driver.current_url)
                print(val)
            else:
                print("Bad URL")
                print(driver.current_url)
                print(val)
            driver.close()

            driver.switch_to.window(win)
        else:
            link.click()
            if driver.current_url == val:
                print("Good URL")
                print(driver.current_url)
                print(val)
            else:
                print("Bad URL")
                print(driver.current_url)
                print(val)
            driver.back()

#kivételkezelés
except NoSuchElementException as e:
    print('Element not found: ', e)

#lezárás
finally:
    driver.close()
