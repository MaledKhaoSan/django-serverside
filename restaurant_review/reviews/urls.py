from django.urls import path
from .views import *

urlpatterns = [
    
    path('create/<int:id>/', ReviewsCreateView.as_view(), name='reviews_create'),
    path('edit/<int:id>/', ReviewsEditView.as_view(), name='reviews_edit'),
    path('delete/<int:id>/', ReviewsDeleteView.as_view(), name='reviews_delete'),
]
