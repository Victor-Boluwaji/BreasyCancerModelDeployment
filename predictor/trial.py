def result(request):
    with open(r"C:\Users\VICTOR\Documents\Backend projects\disease_prediction\Breast_cancer.pkl", 'rb') as f:
        description, model = load(f)
    
    age = request.GET.get('age')
    race_group = request.GET.get('race_group')
    first_degree_hx = request.GET.get('first_degree_hx')
    current_hrt = request.GET.get('current_hrt')
    menopaus = request.GET.get('menopaus')
    bmi = request.GET.get('bmi')
    biophx = request.GET.get('biophx')

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

    if results == 0:
        status = 'Not present'
    else:
        status = 'present'

    '''ModelResults.objects.create(
        age=age, 
        race_group=race_group, 
        first_degree_hx=first_degree_hx, 
        current_hrt=current_hrt, 
        menopaus=menopaus, 
        bmi=bmi, 
        biophx=biophx,
        results=results[0],
        status=status,
        )
    '''
    return render (request, 'result.html',{'results':results[0]} )