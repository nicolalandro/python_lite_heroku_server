import os

from shovel import task


@task
def build():
    """
    This build docker app. Esamples: shovel docker.build
    """
    os.system('docker build -t app/prod -f ./Docker/production/Dockerfile .')


@task
def run():
    """
    This run docker container. Esamples: shovel docker.run
    """
    os.system('docker run --name fish_service --rm -p 5000:5000 -it app/prod')


@task
def stop():
    """
    This build stop all docker container. Esamples: shovel docker.stop
    """
    os.system('docker stop $(docker ps -a -q -f "name=fish_service")')


@task
def remove():
    """
    This build remove all docker container. Esamples: shovel docker.remove
    """
    os.system('docker rm $(docker ps -a -q -f "name=fish_service")')


@task
def bash():
    """
    This provide a shell in docker. Esamples: shovel docker.bash
    """
    os.system('docker exec -it $(docker ps -a -q -f "name=fish_service") /bin/bash')
