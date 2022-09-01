from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def navigate_to_general_page():
    link = driver.find_element(By.XPATH, '//a[text()="General text and other elements"]')
    link.click()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://selenium.oktwebs.training360.com/")
    print(driver.current_url)
    navigate_to_general_page()
    print(driver.current_url)
    driver.back()
    print(driver.current_url)
    navigate_to_general_page()
    anchors = driver.find_elements(By.XPATH, '//header//small//a')

    for a in anchors:
        a.click()
        print(driver.current_url)
    print("*" * 50)
    while driver.current_url != "http://selenium.oktwebs.training360.com/":
        print(driver.current_url)
        driver.back()
finally:
    driver.close()
