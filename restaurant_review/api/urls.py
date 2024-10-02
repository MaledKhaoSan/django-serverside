# restaurant_review/api/urls.py
from django.urls import path
from api.views import ProvinceSearchView

urlpatterns = [
    path('province-search/', ProvinceSearchView.as_view(), name='province_search'),
]
