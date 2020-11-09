from django.shortcuts import render
import requests
import json
from .forms import UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib import messages
from django.shortcuts import redirect


# 6xwXeQBthGPQj7wkQissV3x6m2I1Y4Te
# M4HNsMo19LzIC5wPovMPNb1VWiaAPOFe

# Create your views here.
def weather_home(request, loc_key):
    print(loc_key)
    api = '6xwXeQBthGPQj7wkQissV3x6m2I1Y4Te'
    current_condition_request = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (loc_key, api)
    current_condition_response = requests.get(current_condition_request)
    current_condition_json = json.loads(current_condition_response.text)
    context = {'temperature': current_condition_json[0]['Temperature']['Metric']['Value']}
    context = {'temperature': 10.0}
    return render(request, 'weather_search.html', context)

def login_form(request):
    form = UserLoginForm
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'weather_search.html', {})

    context = {'form': form}
    return render(request, 'login.html', context)

def search_location(request):
    location_dict = {}

    print(request)
    location_key = request.GET['location_key']
    api_key = '6xwXeQBthGPQj7wkQissV3x6m2I1Y4Te'
    autocomplete_request = 'http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=%s&q=%s&language=en-us' % (api_key, location_key)
    autocomplete_response = requests.get(autocomplete_request)
    autocomplete_response_json = json.loads(autocomplete_response.text)

    for i in autocomplete_response_json:
        localized_name_str = i["LocalizedName"] + ", " + i["AdministrativeArea"]["LocalizedName"]
        location_dict.update({i['Key'] : localized_name_str})
    
    # messages.info(request, location_dict)
    context = {'location_dict': location_dict}
    return render(request, 'weather_search.html', context)