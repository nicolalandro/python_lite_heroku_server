# Python Lite Heroku Server
This is a lite heroku server that run python

## How to run
    $ pip install -r requirements.txt
    $ gunicorn main:app --log-file=-

## How to install requirements for test
    $ pip install -r requirements.txt
    $ pip install -r requirements-test.txt
    
## How to USE the pro
    $ heroku logs --app fishserverapi
    $ heroku run bash --app fishserverapi
    
## Deploy Steps
* click deploy on heroku interface
* execute:


    $ heroku run bash --app fishserverapi -c "python set_pcloud_credential.py <uname> <password>"
