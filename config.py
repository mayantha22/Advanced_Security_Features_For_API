import os

class Config:
    DEBUG = True 
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key_if_none_found')
