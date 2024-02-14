from django.contrib import admin
from .models import Console, Product, Tag


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'console',
        'display_tags'
    )

    def get_queryset(self, request):
        """Prefetch the related tags to optimize queries"""
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('tags')
        return queryset

    def display_tags(self, obj):
        """This is required to display tag"""
        return ', '.join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'


admin.site.register(Console)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
