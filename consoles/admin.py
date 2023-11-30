from django.contrib import admin
from .models import Console, Product, Tag, ProductTag, Wishlist


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'console',
        'display_tags'
    )

#     Resources for QuerySet
#     https://docs.djangoproject.com/en/3.2/ref/models/querysets/
#     https://docs.djangoproject.com/en/3.2/ref/models/querysets/#prefetch-related

    def get_queryset(self, request):
        """Prefetch the related tags to optimize queries"""
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('tags')
        return queryset

    def display_tags(self, obj):
        """This is required to display tag"""
        return ', '.join([tag.tag for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'


admin.site.register(Console)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(ProductTag)
admin.site.register(Wishlist)
