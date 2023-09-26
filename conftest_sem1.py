import pytest
import yaml

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
