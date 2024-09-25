from django import forms
from .models import Restaurant, RestaurantType

class RestaurantForm(forms.ModelForm):
    restaurant_types = forms.ModelMultipleChoiceField(
        queryset=RestaurantType.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Change to checkboxes
        required=True
    )
    
    # Make latitude and longitude not required
    latitude = forms.DecimalField(required=False)
    longitude = forms.DecimalField(required=False)
    
    class Meta:
        model = Restaurant
        fields = ['name', 'service_type', 'price_range', 'province', 'district', 'subdistrict', 'latitude', 'longitude', 'restaurant_types']

    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        if latitude is not None and (latitude < -90 or latitude > 90):
            raise forms.ValidationError("Latitude must be between -90 and 90 degrees.")
        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')
        if longitude is not None and (longitude < -180 or longitude > 180):
            raise forms.ValidationError("Longitude must be between -180 and 180 degrees.")
        return longitude

    def clean(self):
        cleaned_data = super().clean()
        service_type = cleaned_data.get('service_type')
        price_range = cleaned_data.get('price_range')

        if not service_type or not price_range:
            raise forms.ValidationError("Both service type and price range are required.")
        
        return cleaned_data
