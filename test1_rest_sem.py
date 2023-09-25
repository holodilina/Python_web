from zeep import Client, Settings

wsdl = 'http://speller.yandex.net/services/spellservice?WSDL'
setting = Settings(strict=False)

client = Client(wsdl=wsdl, settings=settings)
print(client.service.сheckText('брыкэ')[0]['s'])


