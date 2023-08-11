from django.contrib import admin

from products.models import Category, Product, Cart

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'price', 'quantity', 'category', 'image')
    search_fields = ('name',)
    ordering = ('name',)


class CartAdmin(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity')
    extra = 0
