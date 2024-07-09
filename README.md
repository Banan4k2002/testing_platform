# Платформа для тестирования

### Как запустить проект:

Cоздать и активировать виртуальное окружение:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Обновить PIP:

```
pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python backend/manage.py migrate
```

Запустить проект:

```
python backend/manage.py runserver
```

Стартовая страница находится по адресу:

```
http://127.0.0.1:8000/
```

### Как работать с проектом:

Создать суперпользователя:

```
python backend/manage.py createsuperuser
```

Перейти в админ-зону:
```
http://127.0.0.1:8000/admin/
```

Далее следует добавить данные в таблицы

### Особенности работы:

- Отладочная версия работает на sqlite и предоставляет минимальный функционал
- Для замены базы данных на postgresql нужно раскомментировать подключение postgresql в константе DATABASES в settings.py и убрать или закомментировать подключение sqlite