from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import requests
from YelpAPI import get_key

#YELP API Endpoints
#Business Search URL -- 'https://api.yelp.com/v3/businesses/search'

@require_http_methods(["GET"])
def index(request):

    #get method
    if request.method == "GET":
        return render(request, 'pages/index.html')

@require_http_methods(["POST"])
def places(request):

        if request.method == "POST":

            Long = request.POST.get("Longitude")
            Lat = request.POST.get("Latitude")
            Dist = request.POST.get("Distance")
            #Define API Key
            API_KEY = get_key()

            #Define endpoint
            Endpoint = 'https://api.yelp.com/v3/businesses/search'

            #Define header
            Header = {'Authorization' : 'bearer %s' % API_KEY}

            #Define parameters
            Parameters = {'term' : 'food',
                        'limit': 25,
                        'radius' : Dist,
                        'longitude' : Long,
                        'latitude' : Lat}

            #Make a request to yelp API
            yelpRequest = requests.get(url = Endpoint, params = Parameters, headers = Header)

            #Convert json string to a dictionary
            business_data = yelpRequest.json()

            print(business_data)

        return render(request, 'pages/places.html', {'business_data': business_data['businesses']})
