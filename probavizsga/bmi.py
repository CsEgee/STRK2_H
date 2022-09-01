# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# oldal megnyitása
driver.get("http://selenium.oktwebs.training360.com/probavizsga/bmi.html")


# beviteli mezőket kitöltő függvény
def bmicalc(height_in, weight_in):
    hight = driver.find_element(By.ID, "height")
    hight.clear()
    hight.send_keys(height_in)
    weight = driver.find_element(By.ID, "weight")
    weight.clear()
    weight.send_keys(weight_in)
    compute = driver.find_element(By.XPATH, "/html/body/input")
    compute.click()


# Underweight eredmény ellenőrzése, bmicalc függvény hívással
bmicalc(171, 45)

# eredmény elemek megkeresése
output = driver.find_element(By.ID, "output")
comment = driver.find_element(By.ID, "comment")

assert output.text == "15"
assert comment.text == "Underweight"

# Normal eredmény ellenőrzése, bmicalc függvény hívással
bmicalc(185, 65)

output = driver.find_element(By.ID, "output")
comment = driver.find_element(By.ID, "comment")
assert output.text == "19"
assert comment.text == "Normal"

driver.close()
