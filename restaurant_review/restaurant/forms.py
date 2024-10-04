from django import forms
from reviews.models import Restaurant, RestaurantType

class RestaurantCreateForm(forms.ModelForm):
    restaurant_types = forms.ModelMultipleChoiceField(
        queryset=RestaurantType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Restaurant
        fields = ['name', 'price_range', 'no_storefront', 'storefront', 'delivery', 'pickup', 'phone_number', 'province', 'district', 'subdistrict', 'latitude', 'longitude', 'restaurant_types']


class RestaurantEditForm(forms.ModelForm):
    restaurant_types = forms.ModelMultipleChoiceField(
        queryset=RestaurantType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Restaurant
        fields = ['name', 'price_range', 'no_storefront', 'storefront', 'delivery', 'pickup', 'latitude', 'longitude', 'restaurant_types']

# class RestaurantForm(forms.ModelForm):
#     name = forms.CharField(max_length=255)
#     price_range = forms.ChoiceField(choices=Restaurant.PRICE_RANGE_CHOICES)
#     province = forms.CharField(max_length=100, required=False, initial='Unknown')
#     district = forms.CharField(max_length=100, required=False, initial='Unknown')
#     subdistrict = forms.CharField(max_length=100, required=False, initial='Unknown')
    
#     # Make latitude and longitude not required
#     latitude = forms.DecimalField(required=False)
#     longitude = forms.DecimalField(required=False)

#     # Modify the clean methods to handle optional values
#     def clean_latitude(self):
#         latitude = self.cleaned_data.get('latitude')
#         if latitude is not None and (latitude < -90 or latitude > 90):
#             raise forms.ValidationError("Latitude must be between -90 and 90 degrees.")
#         return latitude

#     def clean_longitude(self):
#         longitude = self.cleaned_data.get('longitude')
#         if longitude is not None and (longitude < -180 or longitude > 180):
#             raise forms.ValidationError("Longitude must be between -180 and 180 degrees.")
#         return longitude

#     # Boolean fields for service types
#     no_storefront = forms.BooleanField(required=False)
#     storefront = forms.BooleanField(required=False)
#     delivery = forms.BooleanField(required=False)
#     pickup = forms.BooleanField(required=False)

#     # Multiple choice field for restaurant types
#     restaurant_types = forms.ModelMultipleChoiceField(
#         queryset=RestaurantType.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )
