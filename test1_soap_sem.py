from zeep import Client, Settings
import yaml

with open(config1_sem.yaml) as f:
  data = yaml.safe.load(f)

wsdl = data['wsdl']
setting = Settings(strict=False)

client = Client(wsdl=wsdl, settings=settings)

def check_text(word):
  return client.service.сheckText(word)[0]['s']
  
print check_text('брыкэ')
