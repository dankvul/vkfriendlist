# Build: 
1) `git clone https://github.com/dankvul/vkfriendlist`
2) Setup virtualenv using 
`sudo pip3 install virtualenv`

3) Install virtualenv to your directory:
    `
    	virtualenv venv 
	`
4) Activate venv:
	` vkfriendlist/$ source bin/venv/activate `
5) Install requirements:
	```(venv) vkfriendlist/$ pip install -r requirements.txt```
6) Edit config.py, there should be vars:
```
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    VK_APP_SECURED_KEY = os.environ.get('VK_APP_SECURED_KEY')
    VK_APP_ID = os.environ.get('VK_APP_ID')
    VK_APP_SERVICE_KEY = os.environ.get('VK_APP_SERVICE_KEY')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')
```
7) Init db and configure flask app:
````
    (venv) vkfriendlist/$ export FLASK_APP=wsgi.py
````
Run
	`(venv) tg_exchange/$ gunicorn wsgi:app`

# vkfriendlist
This flask-app use webhook, so, you should firstly deploy source on remote server to fully run it. This app is ready to 
