from django.contrib import admin
from .models import Doctor

from .models import Medicine, Supplier, Order, ContactMessage, Category, CartItem  # ✅ Added Category here



@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'whatsapp_number']
    search_fields = ['name', 'specialization']

# Register your models here
admin.site.register(ContactMessage)
admin.site.register(Medicine)
# admin.site.register(Supplier)
# admin.site.register(Order)
admin.site.register(Category)
admin.site.register(CartItem) 

 # ✅ Registered Category
 # ✅ Registered Category
