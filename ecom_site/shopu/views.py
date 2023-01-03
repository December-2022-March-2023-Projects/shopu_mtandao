from django.shortcuts import render
from .models import Merchandises, Order
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

# Detail view
def detail(request, id):
  merch_object = Merchandises.objects.get(id=id)
  return render(request,'shopu/detail.html', {'merch_object':merch_object})

# Checkout view
def checkout(request):
  if request.method == "POST":
    items = request.POST.get('items', "")
    name = request.POST.get('name',"")
    email = request.POST.get('email',"")
    address = request.POST.get('email',"")
    city = request.POST.get('city',"")
    state = request.POST.get('state',"")
    zipcode = request.POST.get('zipcode',"")
  
    order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode)
    order.save()

  return render(request, 'shopu/checkout.html')
