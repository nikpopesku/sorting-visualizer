#!/bin/bash

echo "Deploy app"
cd /var/www/sorting-visualizer
git reset --hard
git pull origin main
#/home/spacer/.local/bin/pipenv install --python /usr/local/bin/python3.12
#/home/spacer/.local/bin/pipenv run python manage.py migrate --settings config.settings.prod
#/home/spacer/.local/bin/pipenv run python manage.py collectstatic --noinput --settings config.settings.prod

#echo "Restart daemons"
#cat /home/spacer/pwd | sudo -S su -c "/etc/init.d/nginx restart"
#cat /home/spacer/pwd | sudo -S su -c "supervisorctl reread"
#cat /home/spacer/pwd | sudo -S su -c "supervisorctl update sorting_visualizer_daphne"
#cat /home/spacer/pwd | sudo -S su -c "supervisorctl update sorting_visualizer_gunicorn"
#cat /home/spacer/pwd | sudo -S su -c "supervisorctl restart sorting_visualizer_daphne"
#cat /home/spacer/pwd | sudo -S su -c "supervisorctl restart sorting_visualizer_gunicorn"
