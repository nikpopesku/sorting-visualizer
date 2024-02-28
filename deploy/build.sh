#!/bin/bash

echo "Deploy app"
cd /var/www/sorting-visualizer
git reset --hard
git pull origin master
cp -f robots/live.txt robots.txt
pipenv install
pipenv run python manage.py migrate

echo "Restart daemons"
cat /home/spacer/pwd | sudo -S su -c "/etc/init.d/nginx restart"
cat /home/spacer/pwd | sudo -S su -c "supervisorctl reread"
cat /home/spacer/pwd | sudo -S su -c "supervisorctl update visualizer"
cat /home/spacer/pwd | sudo -S su -c "supervisorctl restart visualizer"
