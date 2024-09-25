from django.views.generic import *
from django.shortcuts import render
from django.views import View
from .models import *

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')