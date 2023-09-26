import pytest
import yaml
import module import Site

with open("testdata.yaml") as f:
  testdata = yaml.safe_load(f)
site = Site(testdata["address"])

@pytest.fuxture()
def selector_login():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fuxture()
def selector_pass():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fuxture()
def selector_btn_submit():
    return "button"

@pytest.fuxture()
def selector_err_banner():
    return """//*[@id="app]/main/div/div[2]/h2"""

@pytest.fuxture()
def selector_blog():
    return """//*[@id="app"]/main/div/div[1]/h1"""

pytest.fuxture()
def site():
    site_instance = Site(testdata["address"])
    yeild site_instance
    site_instance.driver.quit()

    
 
