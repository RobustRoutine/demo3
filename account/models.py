from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date

# Create your models here.
Days = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)



class teacher_timetable(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='1')
    day=models.CharField(max_length=50, choices=Days, default='Monday')
    First_lech=models.CharField(max_length=50, null=True,blank=True)
    sec_lech=models.CharField(max_length=50, null=True,blank=True)
    third_lech=models.CharField(max_length=50, null=True,blank=True)
    fourth_lech=models.CharField(max_length=50, null=True,blank=True)
    fifth_lech=models.CharField(max_length=50, null=True,blank=True)
    sixth_lech=models.CharField(max_length=50, null=True,blank=True)
    sev_lech=models.CharField(max_length=50, null=True,blank=True)
    First_link=models.CharField(max_length=50, null=True,blank=True)
    sec_link=models.CharField(max_length=50, null=True,blank=True)
    third_link=models.CharField(max_length=50, null=True,blank=True)
    fourth_link=models.CharField(max_length=50, null=True,blank=True)
    fifth_link=models.CharField(max_length=50, null=True,blank=True)
    sixth_link=models.CharField(max_length=50, null=True,blank=True)
    sev_link=models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return '{} {}'.format(str(self.name),str(self.day))


