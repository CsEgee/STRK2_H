# importok
import time
import filecmp

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = ''

try:

    # oldal megnyitása
    driver.get(URL)



finally:
    driver.close()