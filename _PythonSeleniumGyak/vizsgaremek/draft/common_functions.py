import time

from selenium.webdriver.common.by import By

def login(driver, user, pwd):
    try:
        driver.get('http://10.211.55.3:8084/login.htm')
    except:
        driver.get('http://localhost:8084/login.htm')

    driver.find_element(By.ID, 'username').send_keys(user)
    driver.find_element(By.NAME, 'j_password').send_keys(pwd)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'button').click()


def logout(driver):
    driver.find_element(By.XPATH, '//*[@id="login"]/a[1]').click()

