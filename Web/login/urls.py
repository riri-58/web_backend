from django.urls import path
from login.views import *

urlpatterns = [
    path('', home),
    path('sing_in/', sing_in),
    path('log_in/', log_in),
]