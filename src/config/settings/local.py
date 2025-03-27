import os
import random

from .base import *
from dotenv import dotenv_values


ENV = dotenv_values(os.path.join(BASE_DIR, "local.env"))

SECRET_KEY = ENV.get(
    "DJANGO_SECRET_KEY",
    "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?", k=50)),
)


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'admin_db'),  # 데이터베이스 이름
        'USER': os.environ.get('DB_USER', 'postgres'),  # 데이터베이스 연결할 유저
        'PASSWORD': os.environ.get('DB_PASSWORD', 'postgres'),  # 데이터베이스 연결할 유저의 비밀번호
        'HOST': os.environ.get('DB_HOST', 'localhost'),  # 데이터베이스 연결 시 사용할 Host(ip 주소, localhost=127.0.0.1)
        'PORT': os.environ.get('DB_PORT', 5432),  # 데이터베이스 연결 시 사용할 Port
    }
}