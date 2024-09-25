from django.views.generic import *
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect
from django.views import View
from .models import *


class RestaurantPageListView(View):
    def get(self, request):
        return render(request, 'restaurant.html')

class RestaurantDetailsView(View):
    def get(self, request, id):
        restaurant = get_object_or_404(Restaurant, id=id)
        return render(request, 'restaurant_details.html', {'restaurant': restaurant})


    
# restaurant/views.py
from django.shortcuts import render
from django.views import View
from .forms import RestaurantForm
class RestaurantCreateView(View):
    def get(self, request):
        form = RestaurantForm()
        return render(request, 'restaurant_form.html', {'form': form})

    def post(self, request):
    # Print raw POST data for debugging
    # print("Raw POST data:", request.POST)

        form = RestaurantForm(request.POST)
        if form.is_valid():
            print("SUBMIT")
            print("Form is valid, printing cleaned data:")
            
            # Access cleaned form data directly and print it for testing
            cleaned_data = form.cleaned_data
            name = cleaned_data['name']
            service_type = cleaned_data['service_type']
            price_range = cleaned_data['price_range']
            latitude = cleaned_data['latitude']
            longitude = cleaned_data['longitude']
            restaurant_types = cleaned_data['restaurant_types']
            
            # Print the form data for testing
            print(f"Name: {name}")
            print(f"Service Type: {service_type}")
            print(f"Price Range: {price_range}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            print(f"Restaurant Types: {[str(rt) for rt in restaurant_types]}")

            # Handle the OperatingHour fields
            days_of_week = request.POST.getlist('day_of_week[]')
            opening_times = request.POST.getlist('opening_time[]')
            closing_times = request.POST.getlist('closing_time[]')

            # Print Operating Hours for each entry
            print("\nOperating Hours:")
            for day, opening, closing in zip(days_of_week, opening_times, closing_times):
                print(f"Day: {day}, Opening: {opening}, Closing: {closing}")

            # Return the form with a success message (for testing purposes)
            return render(request, 'restaurant_form.html', {'form': form, 'success': 'Data printed successfully!'})

        # If form is invalid, re-render the form with errors and print errors
        # print("Form is invalid:", form.errors)
        return render(request, 'restaurant_form.html', {'form': form})
