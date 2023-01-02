from django.shortcuts import render
from .models import Merchandises
# Create your views here.

def index(request):
  merch_objects = Merchandises.objects.all()

  item_name = request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    merch_objects = merch_objects.filter(title__icontains=item_name)
  return render(request, 'shopu/index.html',{'merch_objects':merch_objects})