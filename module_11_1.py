import requests
r = requests.get('https://mail.ru')
if r.status_code == 200:
    print(r.text)
else:
    print('Запрос выполнен с ошибкой')