import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestGooglewebtest():
  def setup_method(self, method):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_google_opens(self):
    self.driver.get("https://www.google.com")
    assert "Google" in self.driver.title

  def test_google_search(self):
    self.driver.get("https://www.google.com")
    search = self.driver.find_element(By.NAME, "q")
    search.send_keys("PTA Pakistan")
    search.submit()
    assert "PTA Pakistan" in self.driver.title