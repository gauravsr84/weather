from django.shortcuts import render
import requests
import json
from .forms import UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def weather_home(request):
    api = '6xwXeQBthGPQj7wkQissV3x6m2I1Y4Te'
    location_id = '204519'
    current_condition_request = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (location_id, api)
    current_condition_response = requests.get(current_condition_request)
    current_condition_json = json.loads(current_condition_response.text)
    context = {'temperature': current_condition_json[0]['Temperature']['Metric']['Value']}
    return render(request, 'weatherindex.html', context)

def login_form(request):
    form = UserLoginForm
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('weather_home'))

    context = {'form': form}
    return render(request, 'login.html', context)