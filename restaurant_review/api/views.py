# restaurant_review/api/views.py
from django.http import JsonResponse
from django.views import View
import json, requests



class ProvinceView(View):
    def get(self, request):
        with open('api/json/thai_provinces.json') as file:
            data = json.load(file)
        return JsonResponse(data, safe=False)

class AmphureView(View):
    def get(self, request):
        province_id = request.GET.get('province', None)
        with open('api/json/thai_amphures.json') as file:
            data = json.load(file)
            if province_id:
                data = [d for d in data if d['province_id'] == int(province_id)]  # เฉพาะอำเภอที่อยู่ในจังหวัดที่เลือก
        return JsonResponse(data, safe=False)

class TambonView(View):
    def get(self, request):
        district_id = request.GET.get('district', None)
        with open('api/json/thai_tambons.json') as file:
            data = json.load(file)
            if district_id:
                data = [t for t in data if t['amphure_id'] == int(district_id)]  # เฉพาะตำบลที่อยู่ในอำเภอที่เลือก
        return JsonResponse(data, safe=False)



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
