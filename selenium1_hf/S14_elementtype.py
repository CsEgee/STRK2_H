
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://selenium.oktwebs.training360.com/trickyelements.html")

try:
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    buttontext = button.text

    result = driver.find_element(By.ID, "result")
    resulttext = result.text

    if buttontext in resulttext:
        print("A helyes szöveg jelenik meg az elemek listája alatt! ")
        print(buttontext + " > " + resulttext)
    else:
        print("NEM a helyes szöveg jelenik meg az elemek listája alatt!")
except:
    print("Nincs kattintható gomb az oldalon!")
