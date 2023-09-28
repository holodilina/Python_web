from BaseApp import BasePage
from selenium.webdriver.common.by import By
import loggin

class TestSearchLocators:
  LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
  LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input"""
  LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
  LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app]/main/div/div[2]/h2""")
  
class OperationsHelper(BasePage):
  def enter_login(self, word):
    loggin.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
    login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
    login_field.clear()
    login_field.send_keys(word)
    
  def enter_pass(self, word):
    loggin.info("Click login button")
    loggin.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
    login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
    login_field.clear()
    login_field.send_keys(word)

  def click_login_button(self):
    self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

  def get_error_text(self):
    error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
    text = error_field.text
    loggin.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]})
    return text

  def get_blog (self):
    blog = self.find_element(TestSearchLocators.LOCATOR_BLOG)
    text = blog_text
    loggin.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_BLOG[1]})
    return text


