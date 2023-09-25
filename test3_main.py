import yaml
import module import Site

with open("testdata.yaml") as f:
  testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1():
  x_selector1 = """ """
  input1 = site.find_element("xpath", x_selector1)
  input1.send_keys("test")
  x_selector2 = """ """
  input2 = site.find_element("xpath", x_selector2)
  input2.send_keys("test")

