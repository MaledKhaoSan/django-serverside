from django.urls import path
from .views import *

urlpatterns = [
    path('', RestaurantMainView.as_view(), name='restaurant_main'),
    
    path('category/', RestaurantListView.as_view(), name='restaurant_list'),
    path('<int:id>/', RestaurantDetailsView.as_view(), name='restaurant_details'),
    path('edit/<int:id>/', RestaurantEditView.as_view(), name='restaurant_edit'),
    path('create/', RestaurantCreateView.as_view(), name='restaurant_create'),
    path('delete/<int:id>/', RestaurantDeleteView.as_view(), name='restaurant_delete'),

    path('favourite/<int:restaurant_id>/', RestaurantFavourite.as_view(), name='restaurant_favourite'),
    # path('category/', RestaurantCreateView.as_view(), name='Restaurant List'),
]


