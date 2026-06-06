from django.shortcuts import render
import os
import joblib
import pandas as pd
from .models import PredictionHistory

path = os.path.dirname(__file__)
model = joblib.load(open(os.path.join(path, "house_price_model.pkl"), "rb"))

# Create your views here.

def index(request):
    return render(request, "index.html")


def prediction(request):
    if request.method == "POST":

        medinc = request.POST['medinc']
        houseage = request.POST['houseage']
        averooms = request.POST['averooms']
        avebedrms = request.POST['avebedrms']
        population = request.POST['population']
        aveoccup = request.POST['aveoccup']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        # Prediction
        res = model.predict([[
            medinc,
            houseage,
            averooms,
            avebedrms,
            population,
            aveoccup,
            latitude,
            longitude
        ]])[0].round(2)

        res = res * 100000

        # History Save
        PredictionHistory.objects.create(
            medinc=medinc,
            houseage=houseage,
            averooms=averooms,
            avebedrms=avebedrms,
            population=population,
            aveoccup=aveoccup,
            latitude=latitude,
            longitude=longitude,
            predicted_price=res
        )

        # Current Prediction Show
        return render(
            request,
            "prediction.html",
            {
                "result": res
            }
        )

    return render(request, "prediction.html")


def history(request):

    data = PredictionHistory.objects.all().order_by('-id')

    return render(
        request,
        "history.html",
        {
            "history": data
        }
    )


def about(request):
    return render(request, "about.html")