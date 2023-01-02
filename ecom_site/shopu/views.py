from django.shortcuts import render
from .models import Merchandises
# Create your views here.

def index(request):
  merch_objects = Merchandises.objects.all()
  return render(request, 'shopu/index.html',{'merch_objects':merch_objects})