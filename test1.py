import yaml
import module import Site

with open("testdata.yaml") as f:
  testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1():

  input1 = site.find_element("xpath", x_selector1)
  input1.send_keys("test")
  
  input2 = site.find_element("xpath", x_selector2)
  input2.send_keys("test")
  
  btn = site.find_element("css", btn_selector)
  btn.click()
  
  err_label = site.find_element("xpath", x_selector3)
  
  # print(err_label.text)
  assert err_label.text == "401"
  
button

# test_step1()
