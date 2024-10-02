# restaurant_review/api/nav_forms.py

from reviews.models import RestaurantType

def restaurant_types(request):
    restaurant_types = RestaurantType.objects.all()
    return {'restaurant_types': restaurant_types}


from django import forms
from reviews.models import RestaurantType
class SearchForm(forms.Form):
    province_id = forms.IntegerField(
        widget=forms.HiddenInput(),  # ใช้ HiddenInput เพื่อให้ไม่แสดงในหน้าเว็บ
        required=False
    )
    
    restaurant_type = forms.ModelChoiceField(
        queryset=RestaurantType.objects.all(), 
        required=False
    )