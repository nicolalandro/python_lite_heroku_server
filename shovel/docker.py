import os
from shovel import task


@task
def build():
    """
    This build docker app. Esamples: shovel docker.build
    """
    os.system('docker build -t flask_server .')


@task
def run():
    """
    This run docker container. Esamples: shovel docker.run
    """
    os.system('docker run -d -p 5000:5000 --name fish_service flask_server')

@task
def run_in_console():
    """
    This run docker container. Esamples: shovel docker.run
    """
    os.system('docker run -p 5000:5000 --name fish_service flask_server')

@task
def stop():
    """
    This build stop all docker container. Esamples: shovel docker.stop
    """
    os.system('docker stop $(docker ps -a -q -f "name=fish_service")')

@task
def stop_all():
    """
    This build stop all docker container. Esamples: shovel docker.stop_all
    """
    os.system('docker stop $(docker ps -a -q)')

@task
def remove():
    """
    This build remove all docker container. Esamples: shovel docker.remove
    """
    os.system('docker rm $(docker ps -a -q -f "name=fish_service")')

@task
def remove_all():
    """
    This build remove all docker container. Esamples: shovel docker.remove_all
    """
    os.system('docker rm $(docker ps -a -q)')


@task
def bash():
    """
    This provide a shell in docker. Esamples: shovel docker.bash
    """
    os.system('docker exec -it $(docker ps -a -q -f "name=fish_service") /bin/bash')


@task
def bash_to(container_id):
    """
    This provide a shell in docker. Esamples: shovel docker.bash a0fa2c4438e3
    """
    os.system('docker exec -it ' + container_id + ' /bin/bash')
