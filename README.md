[![GitHub issues](https://img.shields.io/github/issues/nicolalandro/python_lite_heroku_server.svg)](https://github.com/nicolalandro/python_lite_heroku_server/issues)
[![Build Status](https://travis-ci.org/nicolalandro/python_lite_heroku_server.svg?branch=master)](https://travis-ci.org/nicolalandro/python_lite_heroku_server)

# Python Lite Heroku Server
This is a lite heroku server that run python

## How to run
    $ export pcloud_uname="<your_uname>"
    $ export pcloud_password="<your_password>"
    $ pip install -r requirements.txt
    $ gunicorn main:app --log-file=-

### Alternatively you can generate .sh file
    $ pip install -r requirements.txt
    $ shovel generate_run_server_script
* insert your pcloud credential
    $ ./run_server_script.sh

## How to install requirements for test
    $ pip install -r requirements.txt
    $ pip install -r requirements-test.txt
    
## How to USE the heroku server bash
    $ heroku logs --app fishserverapi
    $ heroku run bash --app fishserverapi
    
## Deploy Steps
* Config Variables on heroku
  * pcloud_uname, with pcloud mail
  * pcloud_password, with pcloud password
* click deploy on heroku interface

## Shovel
    $ shovel tasks

## Docker
* shovel docker.build
* shovel docker.run
  * test execution

# Time test webdriver
* firefox set_headless(True)
  * real    2m30.424s
  * user    0m19.989s
  * sys     0m3.418s
* firefox set_headless(False)
  * real    0m23.266s
  * user    0m18.479s
  * sys     0m2.592s
* phanthomJS (ma è deprecato) 
  * real    0m8.498s
  * user    0m1.835s
  * sys     0m0.386s


