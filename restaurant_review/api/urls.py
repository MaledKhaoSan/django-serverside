# restaurant_review/api/urls.py
from django.urls import path
from api.views import ProvinceSearchView, ProvinceView, AmphureView, TambonView

urlpatterns = [
    path('province-search/', ProvinceSearchView.as_view(), name='province_search'),
    path('json/provinces/', ProvinceView.as_view(), name='provinces'),
    path('json/amphures/', AmphureView.as_view(), name='amphures'),
    path('json/tambons/', TambonView.as_view(), name='tambons'),
]
