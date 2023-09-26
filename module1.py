import yaml
import time
from selenium import webdriver
import selenium.webdriver.common.by import By
from selenium.webdriver.chrom.service import Service

with open(".testdata.yaml") as f:
  testdata = yaml.sefe_load(f)

service = Service(testdata["driver_path"])
options = webdriver.ChromeOptions

class Site:
  def __init__(self, address):
    self.driver = webdriver.Chrome(service=service, options=options)
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
