import pytest, yaml
from selenium import webdriver
from selenium.webdriver.chrom.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open(".testdata.yaml") as f:
  testdata = yaml.sefe_load(f)
  browser = testdata["browser"]

@pytest.fixture(scope="session")

def browser():
    if browser == "firefox":
      service = Service(executable_path=GeckoDriverManager().install())
      options = webdriver.FirefoxOptions()
      driver = webdriver.Firefox(service=service, options=options)
    else:
      service = Service(executable_path=ChromeDriverManager().install())
      options = webdriver.ChromeOptions()
      driver = webdriver.Chrome(service=service, options=options)
    yeld driver
    driver.quit()

