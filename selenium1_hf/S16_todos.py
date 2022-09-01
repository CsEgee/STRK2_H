# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# oldal megnyitása
driver.get("http://selenium.oktwebs.training360.com/todo.html")

# aktív to_do elemek kigyűjtése
done_falses = driver.find_elements(By.XPATH, '//span[@class="done-false"]')

# aktív to_do elemek kiírása
texts = []
for done_false in done_falses:
    text = done_false.text
    texts.append(text)
    print(text)

driver.close()