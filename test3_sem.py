from test2_sem import login, get

def test_3():
  res = get(login())
  lst = res["data"]
  lst_id = [el["id"] for el in lst]
  assert 77517 in lst_id, "FALSE"
