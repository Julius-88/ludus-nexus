from django.contrib import admin
from .models import Order, OrderDetail


class OrderDetailAdminInline(admin.TabularInline):
    model = OrderDetail
    readonly_fields = ('orderdetail_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderDetailAdminInline,)
    readonly_fields = ('order_number', 'order_date', 'total_price')

    fields = (
        'order_number',
        'order_date',
        'user',
        'address',
        'postcode',
        'city',
        'payment_method',
        'payment_status',
        'total_price')

    list_display = (
        'order_number',
        'order_date',
        'user',
        'address',
        'postcode',
        'city',
        'payment_method',
        'payment_status',
        'total_price')

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
