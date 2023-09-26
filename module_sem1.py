
import yaml
import time
from selenium import webdriver
import selenium.webdriver.common.by import By
from selenium.webdriver.chrom.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open(".testdata.yaml") as f:
  testdata = yaml.sefe_load(f)
  browser = testdata["browser"]

class Site:
  def __init__(self, address):
    if browser == "firefox":
      service = Service(executable_path=GeckoDriverManager().install)
      options = webdriver.FirefoxOptions()
      self driver = webdriver.Firefox(service=service, options=options)
    elif browser == "chrome":
      service = Service(executable_path=ChromeDriverManager().install)
      options = webdriver.Chrome(service=service, options=options)
      self.driver = webdriver.Chrome(service=service, options=options)

    self.driver.implicitly_wait(testdata_sem1["wait_time"])
    self.driver.maximize_window()
    self.driver.get(address)
    timesleep(testdata["sleep_time"])

def find_element(self, mode, path):
  if mode == "css":
    element = self.driver.find_element(By.CSS_SELECTOR, path)
  elif mode == "xpath":
    element = self.driver.find_element(By.XPATH, path)
  else:
    element = None
  return element

def get_element_property(self, mode, path, property):
  element = self.find_element(mode, path)
  return element.value_of_css_property(property)
  
def close(self):
  self.driver.close()
