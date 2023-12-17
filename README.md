# Secure

## Установка

1. Установите зависимости, выполнив команду:
Так же предварительно установите django-defender и запустите redis на локалхост, затем измените url redis в settings.py
```
pip install -r requirements.txt
```
Примените миграции:
```
python manage.py migrate
```
Запустите сервер разработки:
```
python manage.py runserver
```

В общем я не успел описать заплатки сайта :(
И с django-defender + Redis не очень получилось.

Автор:
Иван Сахневич
