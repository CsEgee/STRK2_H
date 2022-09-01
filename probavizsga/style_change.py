# importok
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# oldal megnyitása
driver.get("http://selenium.oktwebs.training360.com/probavizsga/style_change.html")

# háttérszínek lekérése
hatterszin = driver.find_element(By.ID, "banner-message").value_of_css_property('background-color')
gombszin = driver.find_element(By.TAG_NAME, "button").value_of_css_property('background-color')

# gomb kikeresése
button = driver.find_element(By.TAG_NAME, "button")

# kezdeti háttérszín ellenőrzése
assert hatterszin == "rgba(255, 255, 255, 1)" and gombszin == "rgba(0, 132, 255, 1)"

button.click()
time.sleep(1)

# kattintás után szín ellenőrzése - ez nem megy :/
assert hatterszin == "rgba(0, 132, 255, 1)" and gombszin == "rgba(255, 255, 255, 1)"

driver.close()
