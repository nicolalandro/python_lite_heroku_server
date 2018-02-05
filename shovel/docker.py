import os
from shovel import task


@task
def build():
    """
    This build docker app. Esamples: shovel docker.build
    """
    os.system('docker build -t flask_server .')


@task
def run_server():
    """
    This run docker container. Esamples: shovel docker.run_server
    """
    os.system('docker run -d -p 5000:5000 flask_server')


@task
def stop_all():
    """
    This build stop all docker container. Esamples: shovel docker.stop_all
    """
    os.system('docker stop $(docker ps -a -q)')


@task
def remove_all():
    """
    This build remove all docker container. Esamples: shovel docker.remove_all
    """
    os.system('docker rm $(docker ps -a -q)')


@task
def bash(container_id):
    """
    This provide a shell in docker. Esamples: shovel docker.ssh a0fa2c4438e3
    """
    os.system('docker exec -it ' + container_id + ' /bin/bash')
