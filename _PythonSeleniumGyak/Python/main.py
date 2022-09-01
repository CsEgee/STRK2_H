# for li in 'John':
#     if li == 'o':
#         pass
#     print(li, end=', ')

# importok
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://localhost:8080")
except:
    driver.get("http://selenium.oktwebs.training360.com/index.html")

time.sleep(3)
driver.close()
