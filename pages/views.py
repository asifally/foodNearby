from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
class Geoform(forms.Form):
    Longitude = forms.CharField(max_length = 50)
    Latitude = forms.CharField(max_length = 50)
    Distance = forms.CharField(max_length = 50)

def index(request):
    if request.method == "GET":
        return render(request, 'pages/index.html')
    elif request.method == "POST":
        form = GeoForm(request.POST)
        if form.is_valid():
            return render(request, 'pages/places.html', {'form' : form})

def places(request):
    return render(request, 'pages/places.html')
