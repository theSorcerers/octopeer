#!/usr/bin/env bash

################################################################################
# General
################################################################################

echo 'LC_ALL="en_US.UTF-8"' | sudo tee -a /etc/environment

################################################################################
# Ruby Installation
################################################################################

sudo apt-get update
sudo apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev \
                        libreadline-dev libyaml-dev libsqlite3-dev sqlite3 \
                        libxml2-dev libxslt1-dev libcurl4-openssl-dev \
                        python-software-properties libffi-dev

git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"

git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"

rbenv install 2.3.1
rbenv global 2.3.1
ruby -v

################################################################################
# Bundler Installation
################################################################################

gem install bundler
rbenv rehash

################################################################################
# Rails Dependencies Installation
################################################################################

curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
sudo apt-get install -y nodejs

################################################################################
# PostgreSQL Installation
################################################################################

sudo apt-get install -y postgresql postgresql-contrib libpq-dev

sudo -u postgres psql -c "CREATE USER vagrant WITH CREATEDB;"

################################################################################
# Octopeer Setup
################################################################################

cd ~/octopeer
bundle
rails db:create
