from django.db import models

# Create your models here.
from django.db import models

class PredictionHistory(models.Model):
    medinc = models.FloatField()
    houseage = models.FloatField()
    averooms = models.FloatField()
    avebedrms = models.FloatField()
    population = models.FloatField()
    aveoccup = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    predicted_price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.predicted_price)