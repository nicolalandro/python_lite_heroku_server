from shovel import task


@task
def hello(name):
    """
    This is hello world. Esamples: shovel testing.test.hello '<name>'
    """
    print('Hello, %s' % name)
