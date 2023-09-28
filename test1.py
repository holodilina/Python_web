from testpage_sem1 import OperationsHelper
import logging
import yaml

with open("testdata3_sem3.yaml") as f:
  testdata = yaml.safe_load(f)

def test_step1(browser):
  logging.info("Test1 Starting")
  testpage = OperationsHelper(browser)
  testpage.go_to_site()
  testpage.enter_login("test")
  testpage.enter_pass("test")
  testpage.click_login_button()
  
  assert testpage.get_error_text() == "401"

def test_step2(browser):
# вход в систему
  logging.info("Test2 Starting")
  testpage = OperationsHelper(browser)
  testpage.go_to_site()
  testpage.enter_login(testdata["login"])
  testpage.enter_pass(testdata["password"])
  testpage.click_login_button()
  testpage.get_blog()
  
  assert testpage.get_blog()() == "401"

