import os
from shovel import task


@task
def hello(name):
    """
    This is hello world. Esamples: shovel testing.test.hello '<name>'
    """
    print('Hello, %s' % name)


@task
def run_server():
    """
    This execute app. Esamples: shovel rub_server
    """
    os.system('gunicorn main:app --log-file=-')
