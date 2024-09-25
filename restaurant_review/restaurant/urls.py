from django.urls import path
from .views import *

urlpatterns = [
    path('', RestaurantPageListView.as_view(), name='Foodie'),
    path('<int:id>/', RestaurantDetailsView.as_view(), name='Foodie Details'),
    path('create/', RestaurantCreateView.as_view(), name='restaurant_create'),
]
