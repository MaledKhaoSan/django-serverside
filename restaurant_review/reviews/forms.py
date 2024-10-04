from django import forms
from reviews.models import Review

# class ReviewCreateForm(forms.ModelForm):
#     rating = forms.ChoiceField(
#         choices=[(i, str(i)) for i in range(1, 6)],  # Ratings 1 to 5
#         widget=forms.RadioSelect
#     )
#     images = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={'multiple': True}),
#         required=False
#     )

#     class Meta:
#         model = Review
#         fields = ['rating', 'comment']


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]
    
    rating = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=RATING_CHOICES
    )
    
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = Review
        fields = ['title', 'rating', 'comment']
