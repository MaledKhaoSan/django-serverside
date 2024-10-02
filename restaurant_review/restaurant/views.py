from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from .forms import RestaurantCreateForm, RestaurantEditForm
from reviews.models import *

from api.nav_forms import *


class RestaurantMainView(View):
    def get(self, request):
        return render(request, 'restaurant_main.html')

class RestauranLlistView(View):
    def get(self, request):
        # Create the form
        form = SearchForm(request.GET or None)
        
        # Default province_id = 1 (กรุงเทพฯ)
        default_province_id = 1

        # Get all restaurants
        restaurants = Restaurant.objects.all()

        if form.is_valid():
            province_id = form.cleaned_data.get('province_id') or default_province_id  # Default province if none selected
            restaurant_type = form.cleaned_data.get('restaurant_type')

            # Filter by province (use province_id)
            if province_id:
                restaurants = restaurants.filter(province=province_id)

            # Filter by restaurant type if selected
            if restaurant_type:
                restaurants = restaurants.filter(restaurant_types__id=restaurant_type.id)

    
        return render(request, 'restaurant_list.html', {
            'restaurants': restaurants,
        })


class RestaurantDetailsView(View):
    def get(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        operating_hours = OperatingHour.objects.filter(restaurant=restaurant)
        restaurant_types = restaurant.restaurant_types.all()  # Get all types for the restaurant
        return render(request, 'restaurant_details.html', {
            'restaurant': restaurant,
            'operating_hours': operating_hours,
            'restaurant_types': restaurant_types
        })


    
# restaurant/views.py
from django.shortcuts import render
from django.views import View


# class RestaurantCreateView(View):
#     def get(self, request):
#         form = RestaurantForm()
#         return render(request, 'restaurant_form.html', {'form': form})

#     def post(self, request):
#         # Print raw POST data for debugging
#         # print("Raw POST data:", request.POST)

#         form = RestaurantForm(request.POST)
#         if form.is_valid():
#             print("SUBMIT")
#             print("Form is valid, printing cleaned data:")
            
#             # Access cleaned form data directly and print it for testing
#             cleaned_data = form.cleaned_data
#             name = cleaned_data['name']
#             price_range = cleaned_data['price_range']
#             latitude = cleaned_data['latitude']
#             longitude = cleaned_data['longitude']
#             restaurant_types = cleaned_data['restaurant_types']
            
#             # Boolean service types
#             no_storefront = cleaned_data['no_storefront']
#             storefront = cleaned_data['storefront']
#             delivery = cleaned_data['delivery']
#             pickup = cleaned_data['pickup']
            
#             # Print the form data for testing
#             print(f"Name: {name}")
#             print(f"Price Range: {price_range}")
#             print(f"Latitude: {latitude}")
#             print(f"Longitude: {longitude}")
#             print(f"Restaurant Types: {[str(rt) for rt in restaurant_types]}")
            
#             # Print the boolean service types
#             print(f"No Storefront: {no_storefront}")
#             print(f"Storefront: {storefront}")
#             print(f"Delivery: {delivery}")
#             print(f"Pickup: {pickup}")

#             # Handle the OperatingHour fields (if applicable)
#             days_of_week = request.POST.getlist('day_of_week[]')
#             opening_times = request.POST.getlist('opening_time[]')
#             closing_times = request.POST.getlist('closing_time[]')

#             # Print Operating Hours for each entry
#             print("\nOperating Hours:")
#             for day, opening, closing in zip(days_of_week, opening_times, closing_times):
#                 print(f"Day: {day}, Opening: {opening}, Closing: {closing}")

#             # After successful form handling, you would typically save the data to the database
#             # form.save() # Uncomment this line when ready to save

#             # Return the form with a success message (for testing purposes)
#             return render(request, 'restaurant_form.html', {'form': form, 'success': 'Data printed successfully!'})

#         # If form is invalid, re-render the form with errors and print errors
#         # print("Form is invalid:", form.errors)
#         return render(request, 'restaurant_form.html', {'form': form})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import RestaurantEditForm
from reviews.models import *


class RestaurantCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = RestaurantCreateForm()
        return render(request, 'restaurant_form.html', {'form': form})

    def post(self, request):
        form = RestaurantCreateForm(request.POST)
        if form.is_valid():
            print("Form is valid, saving restaurant...")
            cleaned_data = form.cleaned_data

            # Extract data from the cleaned form
            name = cleaned_data['name']
            price_range = cleaned_data['price_range']
            latitude = cleaned_data['latitude']
            longitude = cleaned_data['longitude']
            restaurant_types = cleaned_data['restaurant_types']

            # Boolean fields
            no_storefront = cleaned_data['no_storefront']
            storefront = cleaned_data['storefront']
            delivery = cleaned_data['delivery']
            pickup = cleaned_data['pickup']

            # Save Restaurant to the database
            restaurant = Restaurant.objects.create(
                name=name,
                price_range=price_range,
                latitude=latitude,
                longitude=longitude,
                no_storefront=no_storefront,
                storefront=storefront,
                delivery=delivery,
                pickup=pickup,
                province=cleaned_data['province'],
                district=cleaned_data['district'],
                subdistrict=cleaned_data['subdistrict'],
                user=request.user  # Ensure the user is logged in
            )

            print(f"Restaurant created successfully with ID: {restaurant.id}")

            # Save restaurant types (many-to-many relationship)
            restaurant.restaurant_types.set(restaurant_types)

            # Save the operating hours
            days_of_week = request.POST.getlist('day_of_week[]')
            opening_times = request.POST.getlist('opening_time[]')
            closing_times = request.POST.getlist('closing_time[]')

            for day, opening, closing in zip(days_of_week, opening_times, closing_times):
                OperatingHour.objects.create(
                    restaurant=restaurant,
                    day_of_week=day,
                    opening_time=opening,
                    closing_time=closing
                )

            print("Operating hours saved successfully.")

            # Redirect to the restaurant list view or show a success page
            return redirect('restaurant_list')  # Replace with the correct URL name for the restaurant list page

        else:
            print("Form is invalid. Errors:", form.errors)

        # If form is invalid, re-render the form with errors
        return render(request, 'restaurant_form.html', {'form': form, 'errors': form.errors})



from django.shortcuts import redirect, render
from reviews.models import Restaurant, OperatingHour
from .forms import RestaurantCreateForm

class RestaurantEditView(View):
    def get(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        operating_hours = OperatingHour.objects.filter(restaurant=restaurant)
        form = RestaurantEditForm(instance=restaurant)
        return render(request, 'restaurant_edit.html', {
            'form': form,
            'restaurant': restaurant,
            'operating_hours': operating_hours,
        })

    def post(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        form = RestaurantEditForm(request.POST, instance=restaurant)

        if form.is_valid():
            # บันทึกข้อมูลร้านอาหารที่อัพเดทแล้ว
            restaurant = form.save()

            # ลบวันทำการเดิมทั้งหมดของร้านอาหาร
            OperatingHour.objects.filter(restaurant=restaurant).delete()

            # รับข้อมูลวันทำการใหม่จากแบบฟอร์ม
            days_of_week = request.POST.getlist('day_of_week[]')
            opening_times = request.POST.getlist('opening_time[]')
            closing_times = request.POST.getlist('closing_time[]')

            # บันทึกวันทำการใหม่
            for day, opening, closing in zip(days_of_week, opening_times, closing_times):
                OperatingHour.objects.create(
                    restaurant=restaurant,
                    day_of_week=day,
                    opening_time=opening,
                    closing_time=closing
                )

            print("Operating hours updated successfully.")
            # หลังจากบันทึกเสร็จ ให้ redirect ไปที่หน้ารายละเอียดของร้านอาหาร
            return redirect('restaurant_details', id=restaurant.id)

        # ถ้า form ไม่ valid, render หน้าเดิมพร้อมกับ error
        return render(request, 'restaurant_edit.html', {
            'form': form,
            'restaurant': restaurant,
            'operating_hours': OperatingHour.objects.filter(restaurant=restaurant),  # ส่งคืนวันทำการเดิมในกรณีที่ form ไม่ valid
        })

from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class RestaurantDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ["reviews.delete_restaurant"]

    def get(self, request, id):
        # ดึงร้านที่ต้องการลบ
        restaurant = Restaurant.objects.get(id=id)
        # ตรวจสอบว่าเป็นเจ้าของหรือไม่ ถ้าไม่ใช่ให้แสดง PermissionDenied
        if restaurant.user != request.user and not request.user.is_staff:
            raise PermissionDenied("คุณไม่มีสิทธิ์ในการลบร้านนี้")

        # ลบร้าน
        restaurant.delete()
        # Redirect ไปที่หน้ารายการร้านอาหารหลังจากลบเสร็จ
        return redirect('restaurant_list')