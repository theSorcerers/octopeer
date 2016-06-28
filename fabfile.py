from fabric.api import *


env.hosts = ['aaronang@octopeer.st.ewi.tudelft.nl']

def deploy():
    with prefix('source ~/env/bin/activate'):
        with cd('~/octopeer'):
            run('git stash')
            run('git pull --rebase')
            run('git stash pop')
            run('python manage.py migrate')
            run('python manage.py loaddata core/fixtures/*.json')
            run('python manage.py collectstatic --noinput')
            sudo('service gunicorn restart')
            sudo('service nginx restart')
