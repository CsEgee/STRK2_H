#importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#driver létrehozása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#elemek kikeresése
try:
    driver.get("http://selenium.oktwebs.training360.com/todo.html")

    todos = driver.find_elements(By.XPATH, '//span[@class="done-false"]')

#műveletek az elemekkel
    print("Active todos:")
    for todo in todos:
        print(todo.text)

#lezárás
finally:
    time.sleep(1.0)
    driver.close()
