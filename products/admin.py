from django.contrib import admin
from parler.admin import TranslatableAdmin
from products.models import Products
class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'description'),
        }),
    )
    def save_model(self, request, obj, form, change):
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)

admin.site.register(Products, ProductAdmin)