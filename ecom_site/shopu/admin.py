from django.contrib import admin
from .models import Merchandises, Order
# Register your models here.

# Modify admin site
admin.site.site_header = "Shop till you drop"
admin.site.site_title = "Merch Shop"
admin.site.index_title = "Manage Merch Shop Shopping"

# list orders
class MerchAdmin(admin.ModelAdmin):

  def adjust_category_to_default(self, request, queryset):
    queryset.update(category="default")
  adjust_category_to_default.short_description = "Default Category"
  list_display = ('title', 'price', 'discount_price', 'category', 'description', 'image')
  search_fields = ('category',)
  actions = ('adjust_category_to_default',)

admin.site.register(Merchandises, MerchAdmin)
admin.site.register(Order)