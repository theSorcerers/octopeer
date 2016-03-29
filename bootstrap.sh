#!/usr/bin/env bash

echo 'LC_ALL="en_US.UTF-8"' >> /etc/environment

apt-get update
apt-get install -y build-essential python-pip python3-dev postgresql postgresql-contrib libpq-dev git

pip install virtualenv django

sudo -u postgres psql -c "CREATE ROLE vagrant WITH PASSWORD 'password' SUPERUSER LOGIN;"
sudo -u postgres psql -c "CREATE DATABASE vagrant OWNER vagrant;"
sudo -u postgres psql -c "CREATE DATABASE octopeer OWNER vagrant;"
