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
        })






class ProfileBookMarkView(View):
    def get(self, request):
        return render(request, 'profile_bookmark.html')
    
class ProfileEditView(View):
    def get(self, request):
        # ดึงข้อมูลจาก auth.User และ UserProfile ที่เกี่ยวข้องกับ user ปัจจุบัน
        user = request.user
        user_profile = user.userprofile

        # รวมข้อมูลจาก User และ UserProfile ใน object เดียว
        context = {
            'profiles': {
                'username': user.username,
                'email': user.email,
                'phone': user_profile.phone_number,
                'about_me': user_profile.about_me,
                'profile_image': user_profile.profile_image
            }
        }

        return render(request, 'profile_edit.html', context)