import getpass
import os
import stat

from shovel import task


@task
def run_server():
    """
    This execute app. Esamples: shovel rub_server
    """
    os.system('gunicorn main:app --log-file=-')


@task
def generate_run_server_script():
    """
    This generate run_server_script.sh inorder to launch serve with it. Esamples: shovel generate_run_server_script
    """
    run_server_file_name = 'run_server_script.sh'
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
