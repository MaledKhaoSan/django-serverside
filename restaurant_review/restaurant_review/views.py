# restaurant/views.py
import requests
from django.shortcuts import render

def province_search(request):
    api_url = 'https://raw.githubusercontent.com/kongvut/thai-province-data/master/api_province.json'
    response = requests.get(api_url)
    provinces = response.json()

    # Render the global nav.html template and pass the provinces data
    return render(request, 'nav.html', {'provinces': provinces})
