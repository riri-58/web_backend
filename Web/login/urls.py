from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_in', views.sing_in, name='sign_in'),
    path('log_in', views.log_in, name='log_in'),
]
