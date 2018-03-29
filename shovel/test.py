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


@task
def run_single(test_method_path):
    """
        This run all test. Esamples: shovel test.run_single acceptance.my_flask_test_case.MyFlaskTestCase.test_xxx
    """
    os.system('python -m unittest test.' + test_method_path)
