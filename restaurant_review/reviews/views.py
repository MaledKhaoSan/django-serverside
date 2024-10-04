from django.shortcuts import render, redirect
from django.views import View
from reviews.models import Restaurant, Review, ReviewImage
from reviews.forms import ReviewForm

class ReviewsCreateView(View):
    def get(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        form = ReviewForm()
        return render(request, 'reviews_create.html', {
            'form': form,
            'restaurant': restaurant
        })

    def post(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            # Save form แต่ยังไม่ commit, ให้มันบันทึก restaurant, user ก่อน
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()

            # Handle multiple images
            images = request.FILES.getlist('image')
            for image in images:
                ReviewImage.objects.create(
                    review=review,
                    image_file=image,
                    uploaded_by=request.user
                )

            # Redirect to the restaurant details page after successful submission
            return redirect('restaurant_details', id=restaurant.id)

        return render(request, 'reviews_create.html', {
            'form': form,
            'restaurant': restaurant
        })
    


class ReviewsEditView(View):
    def get(self, request, id):
        reviews = Review.objects.get(id=id)
        restaurant = Restaurant.objects.get(id=reviews.restaurant.id)
        form = ReviewForm(instance=reviews)  # Pass existing review data to the form
        return render(request, 'reviews_edit.html', {
            'form': form,
            'reviews': reviews,
            'restaurant': restaurant
        })

    def post(self, request, id):
        reviews = Review.objects.get(id=id)
        form = ReviewForm(request.POST, request.FILES, instance=reviews)  # Load form with existing review

        if form.is_valid():
            # ลบภาพที่มีอยู่แล้วก่อนบันทึกภาพใหม่
            reviews.reviewimage_set.all().delete()

            # บันทึกรีวิวที่ถูกแก้ไข
            review = form.save()

            # จัดการกับรูปภาพใหม่ที่ถูกอัปโหลด
            images = request.FILES.getlist('image')  # ดึงไฟล์ภาพที่ถูกส่งมา
            for image in images:
                ReviewImage.objects.create(
                    review=review,
                    image_file=image,
                    uploaded_by=request.user
                )

            return redirect('restaurant_details', id=reviews.restaurant.id)  # Redirect ไปยังหน้ารายละเอียดร้านอาหารหลังบันทึกเสร็จ

        return render(request, 'reviews_edit.html', {
            'form': form,
            'reviews': reviews
        })


# LoginRequiredMixin, PermissionRequiredMixin, 
class ReviewsDeleteView(View):
    # permission_required = ["reviews.delete_Review"]
    def post(self, request, id):
        # ดึงร้านที่ต้องการลบ
        reviews = Review.objects.get(id=id)

        # ตรวจสอบว่าเป็นเจ้าของหรือไม่ ถ้าไม่ใช่ให้แสดง PermissionDenied
        if reviews.user != request.user and not request.user.is_staff:
            print("คุณไม่มีสิทธิ์ในการลบร้านนี้")
            # raise PermissionDenied("คุณไม่มีสิทธิ์ในการลบร้านนี้")

        # ลบร้าน
        reviews.delete()

        # Redirect ไปที่หน้ารายการร้านอาหารหลังจากลบเสร็จ
        return redirect('profile')

