from django.contrib import admin
from .models import Item, Category, Review

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'item', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
