from django.db import models

# Create your models here.

#Class listing the details for each keyword searched.
class Domain(models.Model):
    keyword = models.CharField(max_length=5)
    tk = models.BooleanField(default=False)
    ml = models.BooleanField(default=False)
    ga = models.BooleanField(default=False)
    cf = models.BooleanField(default=False)
    gq = models.BooleanField(default=False)
    length = models.IntegerField()
    checked_date = models.DateTimeField()
    created_date = models.DateTimeField()
