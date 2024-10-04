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
    template_name = 'profile_bookmark.html'

    def get(self, request ):
        # ดึงข้อมูลรายการโปรดของผู้ใช้
        favorites = Favorite.objects.filter(user=request.user).select_related('restaurant')
        # ส่งข้อมูลไปยัง template
        return render(request, self.template_name, {'favorites': favorites})

    
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import *

class ProfileEditView(View):
    template_name = 'profile_edit.html'

    def get(self, request):
        # Fetch the current user's profile and user model
        user = request.user
        user_profile = user.userprofile

        # Prepare the context with user and profile data
        context = {
            'profiles': {
                'username': user.username,
                'email': user.email,
                'phone': user_profile.phone_number,
                'about_me': user_profile.about_me,
                'profile_image': user_profile.profile_image
            }
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        user_profile = user.userprofile

        # Check which part is being updated and update accordingly
        if 'save_profile_picture' in request.POST:
            user_profile.profile_image = request.FILES.get('profile_picture')
            user_profile.save()
            messages.success(request, 'โปรไฟล์รูปถูกเปลี่ยนแล้ว')

        if 'save_name' in request.POST:
            new_name = request.POST.get('user', '').strip()
            if new_name and new_name != user.username:
                user.username = new_name

        if 'save_email' in request.POST:
            new_email = request.POST.get('email', '').strip()
            if new_email and new_email != user.email:
                user.email = new_email

        if 'save_phone' in request.POST:
            new_phone = request.POST.get('phone_number', '').strip()
            if new_phone and new_phone != user_profile.phone_number:
                user_profile.phone_number = new_phone

        if 'save_about_me' in request.POST:
            new_about_me = request.POST.get('about_me', '').strip()
            if new_about_me and new_about_me != user_profile.about_me:
                user_profile.about_me = new_about_me

        # Save changes to both User and UserProfile
        user.save()
        user_profile.save()

        messages.success(request, 'ข้อมูลโปรไฟล์ถูกบันทึกแล้ว')
        return redirect('profile_edit')
    
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from reviews.models import Restaurant, Favorite
    
class AddToFavoritesView(LoginRequiredMixin, View):
    
    def post(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        
        # สร้างหรือดึงรายการโปรดของผู้ใช้
        favorite, created = Favorite.objects.get_or_create(user=request.user, restaurant=restaurant)

        if created:
            message = f'{restaurant.name} ถูกบันทึกในรายการโปรดของคุณ'
        else:
            message = f'{restaurant.name} อยู่ในรายการโปรดของคุณแล้ว'

        # ส่งข้อความตอบกลับในรูปแบบ JSON
        return JsonResponse({'message': message})
    
    
