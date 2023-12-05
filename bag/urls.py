from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name="view_bag"),
    path('checkout/', views.checkout, name="checkout"),
    path('add/<product_id>', views.add_to_bag, name="add_to_bag"),
    path('remove/<product_id>', views.remove_from_bag, name="remove_from_bag"),
    path(
        'order-confirmation/<int:order_id>/',
        views.order_confirmation,
        name='order_confirmation'),
    path('user-orders/', views.user_orders, name='user_orders'),
]
