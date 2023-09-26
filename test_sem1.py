import yaml
import module import Site

with open("testdata.yaml") as f:
  testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1():
  x_selector1 = """//*[@id="login"]/div[1]/label/input"""
  input1 = site.find_element("xpath", x_selector1)
  input1.send_keys("test")
  x_selector2 = """//*[@id="login"]/div[2]/label/input"""
  input2 = site.find_element("xpath", x_selector2)
  input2.send_keys("test")
  btn_selector = "button"
  btn = site.find_element("css", btn_selector)
  btn.click()
  x_selector3 = """//*[@id="app]/main/div/div[2]/h2"""
  err_label = site.find_element("xpath", x_selector3)
  assert err_label.text == "401"
  
def test_step2(selector_login, selector_pass, selector_btn_submit, selector_err_banner):
  input1 = site.find_element("xpath", selector_login)
  input1.send_keys("test")

  input2 = site.find_element("xpath", selector_pass)
  input2.send_keys("test")
  
  btn = site.find_element("css", selector_btn_submit)
  btn.click()
  x_selector3 = """//*[@id="app]/main/div/div[2]/h2"""
  err_label = site.find_element("xpath", x_selector3)
  assert err_label.text == "401"


