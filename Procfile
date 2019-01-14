release: python manage.py migrate
web: gunicorn config.wsgi:application --env DJANGO_SETTINGS_MODULE='config.settings.prod'