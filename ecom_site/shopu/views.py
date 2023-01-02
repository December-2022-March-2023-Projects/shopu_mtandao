from django.shortcuts import render
from .models import Merchandises
from django.core.paginator import Paginator
# Create your views here.

def index(request):
  merch_objects = Merchandises.objects.all()

  # search
  item_name = request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    merch_objects = merch_objects.filter(title__icontains=item_name)

  # paginiator
  paginator = Paginator(merch_objects, 3)
  page = request.GET.get('page')
  merch_objects = paginator.get_page(page)

  return render(request, 'shopu/index.html',{'merch_objects':merch_objects})