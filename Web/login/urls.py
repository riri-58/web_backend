from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_in', views.sing_in, name='sign_in'),
    path('log_in', views.log_in, name='log_in'),
    path('packages', views.packages, name='packages'),
    path('hotels', views.hotels, name='hotels'),
    path('insurance', views.insurance, name='insurance'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('blog_home', views.blog_home, name='blog_home'),
    path('contact', views.contact, name='contact'),
]
