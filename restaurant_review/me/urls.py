from django.urls import path
from .views import *

urlpatterns = [
    
    path('', ProfileView.as_view(), name='profile'),
    path('bookmark/', ProfileBookMarkView.as_view(), name='profile_bookmark'),
    path('edit/', ProfileEditView.as_view(), name='profile_edit')
]