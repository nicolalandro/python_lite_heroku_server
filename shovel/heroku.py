import os

from shovel import task


@task
def logs():
    """
    This show the heroku logs. Esamples: shovel heroku.logs
    """
    os.system('heroku logs --app fishserverapi')


@task
def bash():
    """
    This open a bash to heroku server. Esamples: shovel heroku.bash
    """
    os.system('heroku run bash --app fishserverapi')
