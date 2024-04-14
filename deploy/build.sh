#!/bin/bash

echo "Deploy app"
cd /var/www/sorting-visualizer
git reset --hard
git pull origin main
pipenv install --python /usr/local/bin/python3.12
pipenv run python manage.py migrate --settings config.settings.prod
pipenv run python manage.py collectstatic --noinput --settings config.settings.prod

echo "Restart daemons"
/etc/init.d/nginx restart
supervisorctl reread
supervisorctl update sorting_visualizer_daphne
supervisorctl update sorting_visualizer_gunicorn
supervisorctl restart sorting_visualizer_daphne
supervisorctl restart sorting_visualizer_gunicorn
