import getpass
import os
import stat
from shovel import task


@task
def generate_docker_run_server():
    """
    This build docker app. Esamples: shovel docker.generate_docker_run_server
    """
    run_server_file_name = 'run_server_from_docker.sh'
    uname = input("insert your pcloud uname: ")
    password = getpass.getpass("insert your pcloud password: ")

    # nice to check password from pcloud

    file = open(run_server_file_name, 'w')
    file.write('#!/usr/bin/env bash\n')
    file.write('export pcloud_uname=' + uname + '\n')
    file.write('export pcloud_password=' + password + '\n')
    file.write('gunicorn -b 0.0.0.0:5000 main:app --log-file=-')
    file.close()

    st = os.stat(run_server_file_name)
    os.chmod(run_server_file_name, st.st_mode | stat.S_IEXEC)

    os.system('ls | grep ' + run_server_file_name)


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
    os.system('docker run --name fish_service --rm -it flask_server')


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
