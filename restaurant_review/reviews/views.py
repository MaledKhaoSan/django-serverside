from django.views.generic import *
from django.shortcuts import render, redirect
from django.views import View
from reviews.models import *
from reviews.forms import ReviewCreateForm





class ReviewsCreateView(View):
    def get(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        form = ReviewCreateForm()
        return render(request, 'reviews_create.html', {
            'form': form,
            'restaurant': restaurant
        })

    def post(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        form = ReviewCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            # สร้าง Review object จากข้อมูลที่ได้รับจากฟอร์ม
            review = Review(
                restaurant=restaurant,
                user=request.user,  # กำหนด user ที่ล็อกอิน
                rating=form.cleaned_data['rating'],
                comment=form.cleaned_data['comment'],
                # ตรวจสอบว่ามีการแนบรูปภาพหรือไม่
                image=request.FILES.get('image', None)
            )
            review.save()  # บันทึกข้อมูลลงฐานข้อมูล

            # กลับไปที่หน้ารายละเอียดของร้านอาหาร
            return redirect('restaurant_details', id=restaurant.id)

        # ถ้า form ไม่ valid, render หน้าเดิมพร้อม error
        return render(request, 'reviews_create.html', {
            'form': form,
            'restaurant': restaurant
        })
    
# class ReviewsEditView(TemplateView):
#     template_name = 'reviews_edit.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         # แทนที่การใช้ get_object_or_404 ด้วยการใช้ try-except
#         try:
#             review = Review.objects.get(pk=self.kwargs['pk'])  # ดึงข้อมูล Review โดยใช้ pk
#         except Review.DoesNotExist:
#             raise Http404("รีวิวนี้ไม่มีอยู่ในระบบ")
        
#         images = Image.objects.filter(review=review)  # ดึงรูปภาพที่เชื่อมกับรีวิวนี้
        
#         context['form'] = ReviewEditForm(instance=review)
#         context['images'] = images  # ส่งข้อมูลรูปภาพไปยัง template
#         return context




