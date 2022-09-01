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
    base_url = "http://selenium.oktwebs.training360.com/general.html"
    driver.get(base_url)
    links = driver.find_elements(By.XPATH, '//a')

    for i in links:
        if i.text == '#':
            links.remove(i)

#műveletek az elemekkel
    for link in links:
        val = link.get_attribute('href')
        if link.get_attribute('target'):
            if base_url in val:
                link.click()
                print("Good URL")
                print(val)
                driver.back()
            else:
                print("Bad URL")
                print(val)
                print("not visiting!!!!")
        else:
            if base_url in val:
                link.click()
                print("Good URL")
                print(val)
                driver.back()
            else:
                print("Bad URL")
                print(val)
                print("not visiting!!!!")

#kivételkezelés
except NoSuchElementException as e:
    print('Element not found: ', e)

#lezárás
finally:
    driver.close()
