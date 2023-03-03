from django.db import models
from register.models import Register

class Content(models.Model):
    author = models.ForeignKey(Register, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    descript = models.TextField()
    files = models.TextField()
