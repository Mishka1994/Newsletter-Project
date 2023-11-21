# Mailing Service
Данный сервис разработан для создания и отправки рассылок клиентам.
Для рассылок есть настройка отправки с периодичностью: раз в день, раз в неделю и раз в месяц
Также в сервисе реализован блог для продвижения продукта. 

Команды для запуска проекта:
    1. Клонировать проект на локальный репозиторий: 'git clone git@github.com:Idvri/Mailing_Service.git'

    2. Создать виртуальное окружение внутри проекта: 'python3 -m venv venv'

    3. Установить зависимости проекта в виртуальное окружение: 'pip install -r requirements.txt'

    **Проект запускается с помощью команды: 'python manage.py runserver'**

Команды для запуска задач с периодичностью:

    - 'python manage.py crontab add': запускает все задачи с периодичностью
    - 'python manage.py crontab show': показывает активные задачи
    - 'python manage.py crontab remove': удаляет запущенный задачи

Периодичность реализована с помощью библиотеки django-crontab(докуметация: https://pypi.org/project/django-crontab/) 
