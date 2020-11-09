from django.shortcuts import render
import requests
import json
from .forms import UserLoginForm
from django.http import HttpResponseRedirect
from .models import Weather
from django.utils import timezone

API_KEY = '22a82QMSvdUIkoyvGV10FQAhVyHbMJNm'

# Create your views here.
def weather_home(request, loc_key, area_name):

    current_condition_request = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (loc_key, API_KEY)
    current_condition_response = requests.get(current_condition_request)
    current_condition_json = json.loads(current_condition_response.text)

    weather_obj = Weather.objects.create()
    weather_obj.temperature = current_condition_json[0]['Temperature']['Metric']['Value']
    weather_obj.location_key = loc_key
    weather_obj.area_name = area_name
    weather_obj.date_time_searched = timezone.now()
    weather_obj.save()

    context = {'weather': Weather.objects.all().order_by("-date_time_searched")}

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
    
    autocomplete_request = 'http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=%s&q=%s&language=en-us' % (API_KEY, request.GET['location_key'])
    autocomplete_response = requests.get(autocomplete_request)
    autocomplete_response_json = json.loads(autocomplete_response.text)
    for i in autocomplete_response_json:
        localized_name_str = i["LocalizedName"] + ", " + i["AdministrativeArea"]["LocalizedName"]
        location_key = i['Key']
        location_dict.update({location_key : localized_name_str})

    context = {'location_dict': location_dict}
    return render(request, 'weather_search.html', context)