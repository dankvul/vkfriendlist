import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    VK_APP_SECURED_KEY = os.environ.get('VK_APP_SECURED_KEY')
    VK_APP_ID = os.environ.get('VK_APP_ID')
    VK_APP_SERVICE_KEY = os.environ.get('VK_APP_SERVICE_KEY')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')