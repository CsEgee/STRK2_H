import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://selenium.oktwebs.training360.com/filltablewithsum.html")


def add(p, q, pr):
    product = driver.find_element(By.ID, "product")
    quantity = driver.find_element(By.ID, "quantity")
    price = driver.find_element(By.ID, "price")
    add_button = driver.find_element(By.ID, "add")
    product.clear()
    quantity.clear()
    price.clear()
    product.send_keys(p)
    quantity.send_keys(q)
    price.send_keys(pr)
    add_button.click()


add("Ford", 1, 75000)
add("Audi", 1, 120000)
add("Renault", 1, 50000)
add("Opel", 1, 65000)

time.sleep(3)
driver.close()
