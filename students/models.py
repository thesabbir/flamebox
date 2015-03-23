from django.db import models

# Create your models here.


class Profile(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Result(models.Model):
    student = models.ForeignKey(Profile)
    exam_name = models.CharField(max_length=50)
    result = models.IntegerField()

    def __str__(self):
        return self.student