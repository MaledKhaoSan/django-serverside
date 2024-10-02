# restaurant_review/api/views.py
import requests
from django.http import JsonResponse
from django.views import View

class ProvinceSearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')  # Get the query from the URL parameters
        api_url = 'https://raw.githubusercontent.com/kongvut/thai-province-data/master/api_province.json'
        response = requests.get(api_url)
        provinces = response.json()

        # Filter provinces based on the query
        filtered_provinces = [
            province for province in provinces 
            if query.lower() in province['name_th'] or query.lower() in province['name_en'].lower()
        ]

        # Return filtered provinces as JSON response
        return JsonResponse({'provinces': filtered_provinces})
