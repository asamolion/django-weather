from django.db import models

# Create your models here.

class WeatherModel(models.Model):
    date = models.DateField()
    max_temp = models.FloatField()
    mean_temp = models.FloatField()
    min_temp = models.FloatField()
    max_dew = models.FloatField()
    mean_dew = models.FloatField()
    min_dew = models.FloatField()
    max_humidity = models.FloatField()
    mean_humidity = models.FloatField()
    min_humidity = models.FloatField()
    max_sea_pressure = models.FloatField()
    mean_sea_pressure = models.FloatField()
    min_sea_pressure = models.FloatField()
    max_visibility = models.FloatField()
    mean_visibility = models.FloatField()
    min_visibility = models.FloatField()
    
    