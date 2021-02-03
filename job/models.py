from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=False)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=15,null=False)
    type = models.CharField(max_length=15,null=False)

    def _str_(self):
        return self.user.username


class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=False)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=15,null=False)
    company = models.CharField(max_length=100,null=False)
    type = models.CharField(max_length=15,null=False)
    status = models.CharField(max_length=20,null=False)
    def _str_(self):
        return self.user.username