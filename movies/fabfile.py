from fabric.api import task
from fabric.api import local
from fabric.api import run #ejecuta un comando en un servidor remoto

@task(alias='ls')
def show_dirs():
    print("Hola world")
    run('ls')

def run_deploy_if_test_completed():
    pass