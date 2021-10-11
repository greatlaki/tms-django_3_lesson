from django.urls import path, re_path
<<<<<<< HEAD
from django.views.decorators.cache import cache_page
=======
>>>>>>> origin

from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('', (WomenHome.as_view()), name='home'),
=======
    path('', WomenHome.as_view(), name='home'),
>>>>>>> origin
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]
