from django.db import models
from register.models import Register

class Content(models.Model):
    author = models.ForeignKey(Register, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    descript = models.TextField()
    files = models.TextField()

"""
{
 "name": "zxc?",
 "descript": "Чому не варто звязуватися з zxc?",
 "files": "file:///C:/Users/User/Desktop/requirements.txt",
 "author": [{
  "login": "zxc",
  "passworld": "zxc100-7",
  "email": "zxc@gul.com"
 }]
}
{
 "name": "zxc?",
 "descript": "Чому не варто звязуватися з zxc?",
 "files": "Томушо zxc це СФ!",
 "author_id": 1
}"""
