# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBC():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bC(self):
    self.driver.get("http://www.burkolatcentrum.hu/")
    self.driver.set_window_size(1423, 990)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".custom-logo:nth-child(1)")
    assert len(elements) > 0
  