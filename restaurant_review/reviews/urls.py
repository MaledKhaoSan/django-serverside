from django.urls import path
from .views import *

urlpatterns = [
    
    path('create/<int:id>/', ReviewsCreateView.as_view(), name='reviews_create'),
    # path('edit/', ReviewsEditView.as_view(), name='reviews_edit'),
]
