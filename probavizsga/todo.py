# importok
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# oldal megnyitása
driver.get("http://selenium.oktwebs.training360.com/probavizsga/todo.html")

# új feladat hozzáadása
newtodo = driver.find_element(By.XPATH, '//*[@id="container"]/input')
newtodo.send_keys("Be Smart!", Keys.RETURN)

# TÖRLÉSRE ÉS ELLENŐRZÉSRE ÖTLETEM SINCS

driver.close()