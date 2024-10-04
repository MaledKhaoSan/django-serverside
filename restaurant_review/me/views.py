from django.views.generic import *
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from reviews.models import *



class ProfileView(View):
    def get(self, request):
        # Fetch reviews written by the current user
        user_reviews = Review.objects.filter(user=request.user).order_by('-created_at')

        # Fetch restaurants owned by the current user
        owned_restaurants = Restaurant.objects.filter(user=request.user).order_by('-name')

        print(user_reviews, owned_restaurants)
        return render(request, 'profile.html', {
            'user_reviews': user_reviews,
            'owned_restaurants': owned_restaurants,
            'range': range(5),
        })






class ProfileBookMarkView(View):
    def get(self, request):
        return render(request, 'profile_bookmark.html')
    
class ProfileEditView(View):
    def get(self, request):
        # ส่งข้อมูล request.user ไปยัง template โดยตรง
        return render(request, 'profile_edit.html')