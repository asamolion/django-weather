from django.db import models

# Create your models here.

class WeatherModel(models.Model):
    date = models.DateField()
    max_temp = models.FloatField(default=0, null=True, blank=True)
    mean_temp = models.FloatField(default=0, null=True, blank=True)
    min_temp = models.FloatField(default=0, null=True, blank=True)
    max_dew = models.FloatField(default=0, null=True, blank=True)
    mean_dew = models.FloatField(default=0, null=True, blank=True)
    min_dew = models.FloatField(default=0, null=True, blank=True)
    max_humidity = models.FloatField(default=0, null=True, blank=True)
    mean_humidity = models.FloatField(default=0, null=True, blank=True)
    min_humidity = models.FloatField(default=0, null=True, blank=True)
    max_sea_pressure = models.FloatField(default=0, null=True, blank=True)
    mean_sea_pressure = models.FloatField(default=0, null=True, blank=True)
    min_sea_pressure = models.FloatField(default=0, null=True, blank=True)
    max_visibility = models.FloatField(default=0, null=True, blank=True)
    mean_visibility = models.FloatField(default=0, null=True, blank=True)
    min_visibility = models.FloatField(default=0, null=True, blank=True)
    # max_wind_speed = models.FloatField(default=0, null=True, blank=True)
    # mean_wind_speed = models.FloatField(default=0, null=True, blank=True)
    # max_gust_speed = models.FloatField(default=0, null=True, blank=True)
    # precipitation = models.FloatField(default=0, null=True, blank=True)
    # cloud_cover = models.IntegerField(default=0)
    # events = models.CharField(max_length=100)
    # wind_direction = models.IntegerField()
    