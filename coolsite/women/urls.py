from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('about/', add_page, name='add_page'),
    path('about/', contact, name='contact'),
    path('about/', login, name='login'),
]
