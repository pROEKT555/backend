from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from login.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
]
