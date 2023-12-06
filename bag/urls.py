from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name="view_bag"),
    path('checkout/', views.checkout, name="checkout"),
    path('add/<product_id>', views.add_to_bag, name="add_to_bag"),
    path('remove/<product_id>', views.remove_from_bag, name="remove_from_bag"),
    path(
        'order-receipt/<int:order_id>/',
        views.order_receipt,
        name='order_receipt'),
    path('order-history/', views.order_history, name='order_history'),
    path('success/<int:order_id>/', views.success, name='success'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path(
        'process-payment/<int:order_id>/',
        views.process_payment,
        name='process_payment'),
]
