from django.contrib import admin
from .models import Merchandises, Order
# Register your models here.

# Modify admin site
admin.site.site_header = "Shop till you drop"
admin.site.site_title = "Merch Shop"
admin.site.index_title = "Manage Merch Shop Shopping"

admin.site.register(Merchandises)
admin.site.register(Order)