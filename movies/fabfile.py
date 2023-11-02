from fabric.api import task
from fabric.api import local
from fabric.api import run #ejecuta un comando en un servidor remoto
from fabric.api import env
from fabric.api import prefix
from fabric.api import sudo
from fabric.api import cd

env.hosts = ['165.232.140.48']
env.user = 'aldo'

def deploy():
    with cd('/home/aldo/project/final_bootcamp2/movies'):
        run('git pull')
        with prefix('source env/bin/activate'):
            run('pip install -r requirements2.txt')
            run('python manage.py migrate')

            sudo('systemctl restart movies')
            sudo('systemctl restart nginx')