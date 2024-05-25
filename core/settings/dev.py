from .base import *

NPM_BIN_PATH = "C://Users//dialg//AppData//Roaming//nvm//v20.0.0//npm.cmd"

DEBUG = True

INSTALLED_APPS.append('django_browser_reload')
MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': LOCAL_DB_NAME,
       'USER': LOCAL_DB_USERNAME,
       'PASSWORD': LOCAL_DB_PASSWORD,
       'HOST': LOCAL_DB_IP,
       'PORT': LOCAL_DB_PORT,
   }
}