from django.views.generic import *
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from reviews.models import *
from .forms import ProfileEditForm



class ProfileView(View):
    def get(self, request):
        # Fetch reviews written by the current user
        user_reviews = Review.objects.filter(user=request.user).order_by('-created_at')

        # Fetch restaurants owned by the current user
        owned_restaurants = Restaurant.objects.filter(user=request.user).order_by('-name')

        return render(request, 'profile.html', {
            'user_reviews': user_reviews,
            'owned_restaurants': owned_restaurants,
            'range': range(5),
        })

class ProfileBookMarkView(View):
    def get(self, request ):
        favorites = Favorite.objects.filter(user=request.user).select_related('restaurant')
        return render(request, 'profile_bookmark.html', {
            'favorites': favorites
        })
class ProfileEditView(View):
    def get(self, request):
        # ส่งข้อมูล request.user ไปยัง template โดยตรง
        return render(request, 'profile_edit.html')
        
    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid():
            # บันทึกข้อมูล User ก่อน
            user = request.user
            user.username = request.POST.get('username', user.username)
            user.email = request.POST.get('email', user.email)
            user.save()

            # บันทึกข้อมูล UserProfile ผ่านฟอร์มโดยตรง
            form.save()

            return render(request, 'profile.html')

        return render(request, 'profile_edit.html', {'form': form})