from random import sample
from unittest import result
from django.shortcuts import render
from numpy import int0
import pandas as pd
from django.http import JsonResponse
from pickle import load
import pickle
from .models import PredResults

# Create your views here.

def predictor(request):
    return render(request, 'predictor.html')

def predictor_changes(request):
    #upicklig the model
    with open(r"Breast_cancer.pkl", 'rb') as f:
        description, model = load(f)
        #Collect data from user
    age = request.POST.get('age')
    race_group = request.POST.get('race_group')
    first_degree_hx = request.POST.get('first_degree_hx')
    current_hrt = request.POST.get('current_hrt')
    menopaus = request.POST.get('menopaus')
    bmi = request.POST.get('bmi')
    biophx = request.POST.get('biophx')

    sample = []
    sample.append(age)
    sample.append(race_group)
    sample.append(first_degree_hx)
    sample.append(current_hrt)
    sample.append(menopaus)
    sample.append(bmi)
    sample.append(biophx)

    print(sample)

    results = model.predict([sample])
    
    sample = [age, race_group, first_degree_hx, current_hrt, menopaus, bmi, biophx]
    results = model.predict([sample])

    if results == 0:
        status = 'Not Present'
    else:
        status = 'present'

    PredResults.objects.create(
    age=age, 
    race_group=race_group, 
    first_degree_hx=first_degree_hx, 
    current_hrt=current_hrt, 
    menopaus=menopaus, 
    bmi=bmi, 
    biophx=biophx,
    status=status
    )

    return render(request, 'result.html',{'results':results})

    
