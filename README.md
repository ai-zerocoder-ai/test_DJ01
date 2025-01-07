```
dj/                  # Корневая папка проекта
├── manage.py        # Управляющий файл Django
├── dj/              # Основная конфигурация проекта
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py  # Файл настроек проекта
│   ├── urls.py      # Главный маршрут проекта
│   └── wsgi.py
└── myapp/           # Приложение "myapp"
    ├── __init__.py
    ├── admin.py     # Настройка админки (пусто)
    ├── apps.py      # Конфигурация приложения
    ├── migrations/  # Папка для миграций базы данных
    │   └── __init__.py
    ├── models.py    # Определение моделей (пусто)
    ├── tests.py     # Тесты приложения (пусто)
    ├── urls.py      # Маршруты приложения
    └── views.py     # Обработчики запросов
```
