import os

from shovel import task


@task
def run_server():
    """
    This execute app. Esamples: shovel rub_server
    """
    os.system('gunicorn main:app --log-file=-')
