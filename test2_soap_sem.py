from test1_soap_sem import check_text
import pytest

def test_step1():
  assert 'колбаса' in check_text('брыкэ'), "что-то не так"
  

