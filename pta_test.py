import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestPTAwebtest1():
  def setup_method(self, method):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pTAwebtest1(self):
    self.driver.get("https://www.pta.gov.pk/")
    self.driver.set_window_size(1050, 708)
    self.driver.execute_script("window.scrollTo(0,2298)")
    self.driver.execute_script("window.scrollTo(0,2343)")
    self.driver.execute_script("window.scrollTo(0,4236)")
    assert "PTA" in self.driver.title