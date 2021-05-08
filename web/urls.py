# Essential
from django.urls import path, include

# Parent Application Views
from core.views import APP

# Child Application Views
from api.pardoewray.app import APP as PW_APP
from api.pardoewray.api import API as PW_API

# URL Endpoints
urlpatterns = [

    # PardoeWray
    path(r'pardoewray/', include(PW_APP)),
    path(r'api/', include(PW_API)),

    # App Browser
    path(r'', include(APP)),

]
