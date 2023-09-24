from zeep import Client
wsdl = "https://dds.cryptopro/verify/service.svc?wsdl"
sing = " "

client = Client(wsdl=wsdl)

def test_step1():
  assert.client.service.VerifySignature('CMS', sing)['Result']
  
