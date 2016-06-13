#!/usr/bin/env bash

echo 'LC_ALL="en_US.UTF-8"' | sudo tee -a /etc/environment

sudo apt-get update
sudo apt-get install -y build-essential python-pip python3-dev postgresql postgresql-contrib libpq-dev nginx

sudo -u postgres psql -c "CREATE DATABASE vagrant;"
sudo -u postgres psql -c "CREATE DATABASE octopeer;"
sudo -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE octopeer TO vagrant;"

sudo pip install virtualenv

cd /home/vagrant
virtualenv env -p python3
source env/bin/activate
cd /home/vagrant/octopeer
pip install -r requirements.txt
python manage.py makemigrations corsheaders
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata core/fixtures/*.json

tee -a /home/vagrant/.bash_aliases << EOF
alias octoserver='python /home/vagrant/octopeer/manage.py runserver 0.0.0.0:8000'
EOF

sudo tee -a /etc/init/gunicorn.conf << EOF
description "Gunicorn application server handling Octopeer"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid vagrant
setgid www-data
chdir /home/vagrant/octopeer

exec /home/vagrant/env/bin/gunicorn --workers 3 --bind unix:/home/vagrant/octopeer.sock octopeer.wsgi:application
EOF

sudo service gunicorn start

sudo tee -a /etc/nginx/sites-available/octopeer << EOF
server {
    client_max_body_size 20M;
    listen 80;
    server_name 10.0.22.6;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/vagrant/octopeer;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/vagrant/octopeer.sock;
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/octopeer /etc/nginx/sites-enabled
sudo service nginx restart
