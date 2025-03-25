# FirstDjango_24032025

## Инструкция по развертыванию

1. 'python3 -m venv django_venv'

2. 'source django_venv/bin/activate'

3. 'pip install -r requirment.txt'

4. 'python manage.py migrate'

5. 'python manage.py runserver'

## Запуск 'ipython' в контексте прилоений 'django'

python manage.py shell_plus --ipython

## Выгрузить данные из БДД

python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json

## Загрузить данные в БД

python manage.py loaddata ./fixtures/items.json

## Дополнительно

1. Полезное ополнение дл шаблонов 'Django'

Добавить в 'settings.json'

"emmet.includeLanguages": {
    "django-html": "html",
}
"files.associations": {
    "*.html" "django-html
}