from django.db import models
from register.models import Register

class Content(models.Model):
    author = models.ForeignKey(Register, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    descript = models.TextField()
    files = models.TextField()


class Tests(models.Model):
    author = models.ForeignKey(Register, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

class Question(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_true = models.BooleanField(default=False)

