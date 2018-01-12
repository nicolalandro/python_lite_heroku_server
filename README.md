# Python Lite Heroku Server
This is a lite heroku server that run python

## How to run
    $ export pcloud_uname="<your_uname>"
    $ export pcloud_password="<your_password>"
    $ pip install -r requirements.txt
    $ gunicorn main:app --log-file=-

## How to install requirements for test
    $ pip install -r requirements.txt
    $ pip install -r requirements-test.txt
    
## How to USE the pro
    $ heroku logs --app fishserverapi
    $ heroku run bash --app fishserverapi
    
## Deploy Steps
* Config Variables on heroku
  * pcloud_uname, with pcloud mail
  * pcloud_password, with pcloud password
* click deploy on heroku interface



