# Essential
from django.urls import path, re_path, include

# Application Views
from api.pardoewray.urls import urlpatterns as PW
from api.views import *
from core.views import *
from tools.server.api import *

# URL Endpoints
urlpatterns = [
    path(r'pardoewray/', include(PW))
]
