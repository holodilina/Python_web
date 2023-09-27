from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TestSearchLocators:
  LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
  LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input"""
  LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
  LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app]/main/div/div[2]/h2""")
  
