from django.shortcuts import render
import pickle

def home(request):
    return render(request, "home.html")

def result(request):
    area = int(request.GET['house_area'])
    result = getPrediction(area)
    return render(request, "result.html", {"result" : result})

def getPrediction(area):
    model = pickle.load(open('model_pickle', 'rb'))
    return model.predict([[area]])