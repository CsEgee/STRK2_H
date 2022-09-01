# importok
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# űrlap mezőinek kattintása és validációs üzenet ellenőrzése
try:
    # oldal betöltése
    driver.get("http://selenium.oktwebs.training360.com/simplevalidation.html")

    # email validátor
    email = driver.find_element(By.ID, 'test-email')
    email.click()
    email.send_keys(Keys.TAB)
    time.sleep(2)
    email_error = driver.find_element(By.XPATH,
                                      "//*[@id='test-email']/../../div[@class='validate-field-error-message']")
    assert email_error.text == "Please enter an e-mail"

    # random field validátor
    random_field = driver.find_element(By.ID, 'test-random-field')
    random_field.click()
    random_field.send_keys("asdf")
    time.sleep(2)
    random_field_error = driver.find_element(By.XPATH,
                                             "//*[@id='test-random-field']/../../div[@class='validate-field-error-message']")
    assert random_field_error.text == 'Should contain "twelve"'

    # card number validátor
    card_number = driver.find_element(By.NAME, 'cardNumber')
    card_number.click()
    card_number.send_keys(Keys.TAB)
    time.sleep(2)
    card_number_error = driver.find_element(By.XPATH,
                                            "//*[@id='test-card-number']/../../div[@class='validate-field-error-message']")
    assert card_number_error.text == "Please enter a credit card number (no spaces)"
finally:
    driver.close()
