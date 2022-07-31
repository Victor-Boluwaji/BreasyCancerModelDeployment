from django.contrib import admin

from predictor.models import PredResults
from .models import PredResults
# Register your models here.

admin.site.register(PredResults)