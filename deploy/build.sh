#!/bin/bash

echo "Deploy app"
cd /var/www/sorting-visualizer
git reset --hard
git pull origin main
pipenv install --python /usr/local/bin/python3.11
pipenv run daphne -b 0.0.0.0 -p 8001 visualizer.asgi:application --settings config.settings.prod
pipenv run python manage.py migrate --settings config.settings.prod
pipenv run python manage.py collectstatic --noinput --settings config.settings.prod

#echo "Restart daemons"
#cat /home/spacer/pwd | sudo -S su -c "/etc/init.d/nginx restart"
#cat /home/spacer/pwd | sudo -S su -c "supervisorctl reread"
#cat /home/spacer/pwd | sudo -S su -c "supervisorctl update visualizer"
#cat /home/spacer/pwd | sudo -S su -c "supervisorctl restart visualizer"
