import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def calculate_bmi(height, weight):  # return text with the appropriate comment
    try:
        driver.get("http://selenium.oktwebs.training360.com/probavizsga/bmi.html")
        time.sleep(3)

        height_input = driver.find_element(By.ID, "height")
        weight_input = driver.find_element(By.ID, "weight")
        submit_button = driver.find_element(By.XPATH, "//input[@value='computeBMI']")

        # needs to clear input fields before typing new data
        height_input.clear()
        weight_input.clear()

        height_input.send_keys(height)
        weight_input.send_keys(weight)
        submit_button.click()
        return driver.find_element(By.ID, "comment").text
    except Exception as e:
        print('Exception occured: ', e)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://selenium.oktwebs.training360.com/probavizsga/bmi.html")

    height_input = driver.find_element(By.ID, "height")
    weight_input = driver.find_element(By.ID, "weight")
    submit_button = driver.find_element(By.XPATH, "//input[@value='computeBMI']")

    # scenario 1 171 cm 45 kg === "Underweight"
    height_input.send_keys("171")
    weight_input.send_keys("45")
    submit_button.click()
    comment_text = driver.find_element(By.ID, "comment").text
    assert comment_text == "Underweight"

    # need to clear input fields before typing new data
    height_input.clear()
    weight_input.clear()

    # scenario 2 185 cm 65 kg === "Normal"
    height_input.send_keys("185")
    weight_input.send_keys("65")
    submit_button.click()
    comment_text = driver.find_element(By.ID, "comment").text
    assert comment_text == "Normal"

except Exception as e:
    print('Exception occured: ', e)

comment = calculate_bmi(171, 45)
assert (comment == "Underweight")

comment = calculate_bmi(185, 65)
assert (comment == "Normal")

driver.close()
