from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://selenium.oktwebs.training360.com/probavizsga/todo.html")
    time.sleep(1)

    """basic nr of todos"""
    list_todos_basic = len(driver.find_elements(By.TAG_NAME, "span"))

    """add new todo"""
    add_new_todo_input = driver.find_element(By.XPATH, '//input[@placeholder="Add new todo"]')
    add_new_todo_input.send_keys("Go to Hogsmeade in the weekend")
    add_new_todo_input.send_keys("\n")
    new_todo = driver.find_element(By.XPATH, f'//*[@id="container"]/ul/li[{list_todos_basic + 1}]').text

    """check of new todo creation"""
    assert len(driver.find_elements(By.TAG_NAME, "span")) == list_todos_basic + 1
    assert new_todo == "Go to Hogsmeade in the weekend"
    assert driver.find_element(By.XPATH, f'//*[@id="container"]/ul/li[{list_todos_basic + 1}]').is_enabled()
    assert driver.find_element(By.XPATH, f'//*[@id="container"]/ul/li[{list_todos_basic + 1}]').is_displayed()
    time.sleep(1)

    """delete the new todo item"""
    driver.find_element(By.XPATH, f'//*[@id="container"]/ul/li[{list_todos_basic + 1}]/span/i').click()
    time.sleep(1)

    """check of deletion new todo item"""
    assert len(driver.find_elements(By.TAG_NAME, "span")) == list_todos_basic


except Exception as e:
    print('Exception occured: ', e)
finally:
    driver.close()
