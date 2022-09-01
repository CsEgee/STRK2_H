# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# linkek listázása
try:
    driver.get("http://selenium.oktwebs.training360.com/")
    links = driver.find_elements(By.TAG_NAME, 'a')
    with open('linkek.txt', 'w') as f:
        for link in links:
            f.write("%s\n" % link.get_attribute('href'))
    f.close()
    with open('linkek.txt', 'a') as f:
        f.write("linkek száma: " + str(len(links)))
    f.close()
finally:
    driver.close()
