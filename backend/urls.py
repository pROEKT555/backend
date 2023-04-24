from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from register.views import RegisterView, LoginView
from content.views import *
from auto_rating.views import index


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('content/', ContentView.as_view(), name='content'),
    path('test/', TestView.as_view(), name='test'),
    path('test/test_info/', TestInfoView.as_view(), name='test_info'),
    path('check/', CheckView.as_view(), name='check'),
    path('auto_rating/', index, name='auto_rating'),
    path('admin/', admin.site.urls),
]
