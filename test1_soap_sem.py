from zeep import Client, Settings

wsdl = 'http://speller.yandex.net/services/spellservice?WSDL'
setting = Settings(strict=False)

client = Client(wsdl=wsdl, settings=settings)

def check_text(word):
  return client.service.сheckText(word)[0]['s']
  
print check_text('брыкэ')
