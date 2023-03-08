from django.db import models

class Register(models.Model):
    login = models.CharField(max_length=100)
    passworld = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
