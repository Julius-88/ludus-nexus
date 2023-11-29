from django.contrib import admin
from .models import Console, Product, Tag, ProductTag, Wishlist


admin.site.register(Console)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(ProductTag)
admin.site.register(Wishlist)
