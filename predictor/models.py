from django.db import models
from django.forms import IntegerField

# Create your models here.

class PredResults(models.Model):
    age = models.IntegerField()
    race_group = models.IntegerField()
    first_degree_hx = models.IntegerField()
    current_hrt = models.IntegerField()
    menopaus = models.IntegerField()
    bmi = models.IntegerField()
    biophx = models.IntegerField()
    status = models.CharField(max_length=300)

    def __str__(self):
        return self.status