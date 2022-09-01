# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# oldal megnyitása
driver.get("http://selenium.oktwebs.training360.com/kitchensink.html")

# elemek kikeresése és szöveges tartalmuk / attribútumuk kiírása
by_ID = driver.find_element(By.ID, "openwindow")
print("by ID, text: " + by_ID.text)

by_ID_2 = driver.find_element(By.ID, "hondacheck")
print("by ID, value attribute: " + by_ID_2.get_attribute("value"))

by_NAME = driver.find_element(By.NAME, "cars")
print("by NAME, value attribute: " + by_NAME.get_attribute("value"))

by_XPATH = driver.find_element(By.XPATH, "//html/body/div[3]/div[3]/fieldset/legend")
print("by XPATH, text: " + by_XPATH.text)

by_XPATH_2 = driver.find_element(By.XPATH, '//button[@id="openwindow"]')
print("by XPATH, text: " + by_XPATH_2.text)

driver.close()

