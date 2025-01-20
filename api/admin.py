from django.contrib import admin
from .models import Category, Product, Order,Wishlist,Review

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')

# Review Admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'rating', 'comment', 'created_at')
    list_filter = ('rating',)
    search_fields = ('product__name', 'comment')

# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'ordered_at')
    search_fields = ('product__name',)

# Wishlist Product
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display =('id','user','product','added_at',)
    search_fields = ('id',)
