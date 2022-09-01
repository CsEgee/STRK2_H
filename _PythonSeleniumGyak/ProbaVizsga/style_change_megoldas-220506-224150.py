import time

from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

try:
    driver.get("http://selenium.oktwebs.training360.com/probavizsga/style_change.html")
    banner_message_div = driver.find_element(By.ID, "banner-message")
    time.sleep(3)
    # the blue button on white background is the default css style with no additional class attribute filled
    assert banner_message_div.get_attribute("class") == ''
    button = driver.find_element(By.XPATH, "//button")
    button.click()
    banner_message_div = driver.find_element(By.ID, "banner-message")
    time.sleep(3)
    # the white button on blue background is the alt css style, thus the class attribute should be 'alt'
    assert banner_message_div.get_attribute("class") == "alt"
except Exception as e:
    print('Exception occured: ', e)
finally:
    driver.close()