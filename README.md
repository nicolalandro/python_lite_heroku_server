[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b097340415c44edda4e98a818f4172eb)](https://app.codacy.com/app/nicolalandro/python_lite_heroku_server?utm_source=github.com&utm_medium=referral&utm_content=nicolalandro/python_lite_heroku_server&utm_campaign=Badge_Grade_Dashboard)
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
* Config Variables on heroku app
  * pcloud_uname, with pcloud mail
  * pcloud_password, with pcloud password
* (or use [terraform](https://www.terraform.io/))
  * set heroku credential in ./terraform/provider.tf
    * use ``` heroku auth:token ``` from command line to obtain your heroku api key
  * change (optionally) the name of app in ./terraform/main.tf
  * set your pcloud credential in config var into ./terraform/main.tf
  * now execute
    * terraform init
    * terraform plan -out plan
    * terraform apply plan
    * (if you want destroy) terraform destroy
* click deploy on heroku interface

## Shovel
    $ shovel tasks

## Docker
* test execution
  * shovel docker.test.build
  * shovel docker.test.run
* prod execution
  * (modify the ENV in ./Docker/production/Dockerfile)
  * shovel docker.prod.build
  * shovel docker.prod.run

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


