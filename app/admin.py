from django.contrib import admin
from .models import Product, CartItem
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description','category', 'product_image_display')  
    search_fields = ('name', 'description')  
    # Custom method to display product image as clickable
    def product_image_display(self, obj):
        if obj.image:  
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="50" height="50" style="object-fit: cover;" /></a>',
                obj.image.url,  # Link to the full-size image
                obj.image.url   # Thumbnail image
            )
        return '-'
    
    product_image_display.short_description = 'Product Image'
admin.site.register(Product, ProductAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'get_total_price')
    search_fields = ('product__name', 'user__username')
    

admin.site.register(CartItem, CartItemAdmin)