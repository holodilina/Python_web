from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TestSearchLocators:
  x_selector1 = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
  x_selector2 = (By.XPATH, """//*[@id="login"]/div[2]/label/input"""
  btn_selector = (By.CSS_SELECTOR, "button")
  x_selector3 = (By.XPATH, """//*[@id="app]/main/div/div[2]/h2""")
  
