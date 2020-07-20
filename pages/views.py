from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import requests
from YelpAPI import get_key
from django.contrib.gis.geoip2 import GeoIP2

#YELP API Endpoints
#Business Search URL -- 'https://api.yelp.com/v3/businesses/search'


@require_http_methods(["GET"])
def index(request):

    #if the form returns a get method, then return the index route
    if request.method == "GET":
        return render(request, 'pages/index.html')

@require_http_methods(["POST"])
def places(request):
        #When the form on the index.html file is submitted, it's action is post to this route
        if request.method == "POST":


            #Grab the contents of the form from the home page
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
                        'limit': 50,
                        'radius' : Dist,
                        'longitude' : Long,
                        'latitude' : Lat,
                        'sort_by' : 'distance',
                        'offset' : 0}

            #Make a request to yelp API
            yelpRequest = requests.get(url = Endpoint, params = Parameters, headers = Header)

            #Convert json string to a dictionary
            business_data = yelpRequest.json()


        return render(request, 'pages/places.html', {'business_data': business_data['businesses']})
