from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://selenium.oktwebs.training360.com/trickybuttons.html")
    buttons = driver.find_elements(By.XPATH, '//button')
    print(buttons)
    print(type(buttons))

    for button in buttons:
        button.click()
        result = driver.find_element(By.XPATH, '//Label[@id="result"]')
        print(result.text)
        assert (result.text == f"{button.text} was clicked")
finally:
    driver.close()
