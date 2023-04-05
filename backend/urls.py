from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from register.views import RegisterView, LoginView
from content.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('content/', ContentView.as_view(), name='content'),
    path('test/', TestView.as_view(), name='test'),
    path('check/', CheckView.as_view(), name='check'),
    path('admin/', admin.site.urls),
]
