from django import forms
from reviews.models import UserProfile

class ProfileEditForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)
    phone_number = forms.CharField(required=False)
    about_me = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = UserProfile
        fields = ['profile_image', 'phone_number', 'about_me']