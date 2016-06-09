from fabric.api import *


env.hosts = ['octopeer@146.185.128.124']

def deploy():
    with prefix('source /home/octopeer/env/bin/activate'):
        with cd('/home/octopeer/octopeer'):
            run('git stash')
            run('git pull --rebase')
            run('git stash pop')
            run('python manage.py migrate')
            run('python manage.py loaddata core/fixtures/*.json')
            run('python manage.py collectstatic --noinput')
            sudo('service gunicorn restart')
            sudo('service nginx restart')
