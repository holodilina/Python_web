import yaml
import time
from selenium import webdriver
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
