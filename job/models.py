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

class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100,null=False)
    salary = models.FloatField(max_length=20)
    image = models.FileField()
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()
    def _str_(self):
        return self.title