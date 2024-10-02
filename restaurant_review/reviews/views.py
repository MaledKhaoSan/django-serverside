from django.views.generic import *
from django.shortcuts import render
from django.views import View
from .models import *



class ReviewsCreateView(View):
    def get(self, request):
        return render(request, 'reviews_create.html')
    
class ReviewsEditView(View):
    def get(self, request):
        return render(request, 'reviews_edit.html')
    