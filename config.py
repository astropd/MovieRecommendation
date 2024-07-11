import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS')
