from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=100, blank=True)
    roll_no = models.IntegerField()
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=20, null=True)
