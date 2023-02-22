from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from register.views import RegisterView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
]
