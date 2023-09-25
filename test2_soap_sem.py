from test1_soap_sem import check_text
import pytest

def test_step1(good, bad):
  assert good in check_text(bad), "что-то не так"


  

