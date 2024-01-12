# hunter_api
## Встановлення пакета 
pip install hunter_api
## Анотація:
1. Тестове завдання від компанії Forager.ai.
2. Автоматичний пошук даних через сайт https://api.hunter.io.
- HunterClient('email_verifier', api_key) - перевірка емейлу.
- HunterClient('email_finder', api_key) - пошук емейлу.
- HunterClient('domain_search', api_key) - пошук емейлу.
- Виконано як CRUD:
  - instance.create('kolesnik.d.i@gmail.com') - запит інформації.
  - instance.read('kolesnik.d.i@gmail.com') - повернення даних у Json форматі
  - instance.update('kolesnik.d.i@gmail.com', 'segareta@ukr.net') - заміна даних одного запиту на інший.
  - instance.delete('segareta@ukr.net') - видалення запиту
3. Типізація коду за вимогами в файлі setup.cfg:
- Вимоги P103, WPS305, WPS332, WPS221 зумисно не оброблені так як ведуть до необгрунтованого збільшення коду без його
поліпшення.
