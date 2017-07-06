import csv
from weather.models import WeatherModel
from datetime import date
from django.utils import timezone

from django.core.management.base import BaseCommand



class Command(BaseCommand):
    def handle(self, **options):
        with open('madrid.csv', 'r') as csvfile:
            lines = csv.DictReader(csvfile)
            for line in lines:
                print(line)
    
