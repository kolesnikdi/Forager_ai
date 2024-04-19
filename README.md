Description in English and Ukrainian
# hunter_api
Integration of some APIs of the https://api.hunter.io website is done as a pip installation package 
## Installing the package  
pip install hunter_api
## Features:
- HunterClient('email_verifier', api_key) --> email verification.
- HunterClient('email_finder', api_key) ---> search for an email.
- HunterClient('domain_search', api_key) --> search for an domain.
- Методи виконані як CRUD:
  - instance.create('enter_email') --> request for information.
  - instance.read('enter_email') --> returning data in JSON
  - instance.update('enter_email', 'enter_email') --> replacing the data of one request with another.
  - instance.delete('enter_email') --> delete a request
## Typing code according to requirements in a file setup.cfg:
- cd .\hunter_api\                       
- flake8 classes.py
- The requirements of P103, WPS305, WPS332, WPS221 were deliberately ignored as they lead to an unreasonable increase in code without its
improvement.

# hunter_api
Інтеграція деяких API сайту https://api.hunter.io виконана як пакет інсталяції pip 
## Встановлення пакета 
pip install hunter_api
## Функціонал:
- HunterClient('email_verifier', api_key) --> перевірка емейлу.
- HunterClient('email_finder', api_key) --> пошук емейлу.
- HunterClient('domain_search', api_key) --> пошук домену.
- Методи виконані як CRUD:
  - instance.create('enter_email') --> запит інформації.
  - instance.read('enter_email') --> повернення даних у JSON
  - instance.update('enter_email', 'enter_email') --> заміна даних одного запиту на інший.
  - instance.delete('enter_email') --> видалення запиту
## Типізація коду за вимогами в файлі setup.cfg:
- cd .\hunter_api\                       
- flake8 classes.py
- Вимоги P103, WPS305, WPS332, WPS221 зумисно проігноровані так як ведуть до необгрунтованого збільшення коду без його
поліпшення.
