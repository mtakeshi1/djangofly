from django.db import models

# Create your models here.


class MenuEntry(models.Model):
    entry_date = models.DateField('date of the entry')
    entry_time = models.CharField(max_length=255)
    entry = models.CharField(max_length=1500)


class DailyActivity(models.Model):
    day_of_week = models.CharField(max_length=10)
    time_slot = models.CharField(max_length=255)