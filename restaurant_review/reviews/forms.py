from django import forms
from reviews.models import *

class ReviewCreateForm(forms.Form):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # ตัวเลือกสำหรับคะแนน 1-5

    rating = forms.ChoiceField(
        choices=RATING_CHOICES, 
        required=True,
        widget=forms.RadioSelect  # ใช้ RadioSelect widget เพื่อให้การแสดงผลเป็น radio buttons
    )
    comment = forms.CharField(widget=forms.Textarea, required=True)
    image = forms.ImageField(required=False)


# class ReviewEditForm(forms.ModelForm):
#     class Meta:
#         model = Review  # ใช้โมเดล Review
#         fields = ['comment', 'rating']  # ใช้เฉพาะฟิลด์ comment และ rating
        
#         # ปรับแต่ง widget ของฟิลด์ในฟอร์ม
#         widgets = {
#             'comment': forms.Textarea(attrs={
#                 'class': 'w-full p-2 border border-gray-300 rounded',
#                 'placeholder': 'แสดงความคิดเห็นของคุณที่นี่...',
#                 'rows': 5,
#             }),
#             'rating': forms.RadioSelect(choices=[(i, '★' * i) for i in range(1, 6)], attrs={
#                 'class': 'star-radio',
#             }),
#         }
        
#         # กำหนด label สำหรับฟิลด์
#         labels = {
#             'comment': 'ความคิดเห็น',
#             'rating': 'ให้คะแนนร้านอาหารนี้',
#         }