import os

from shovel import task


@task
def run_acceptance():
    """
    This run all acceptance test. Esamples: shovel test.run_acceptance
    """
    os.system('python -m unittest discover -s test/acceptance --pattern=*.py 1>&2')


@task
def run_all():
    """
    This run all test. Esamples: shovel test.run_all
    """
    os.system('python -m unittest discover -s test --pattern=*test.py 1>&2')
