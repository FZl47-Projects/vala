from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/add/', views.AddProductView.as_view(), name='add_product'),
    path('products/<int:pk>/delete/', views.DeleteProductView.as_view(), name='delete_product'),
    path('products/order/add/', views.AddOrderRequestView.as_view(), name='add_order_request'),
    path('products/order/list/', views.OrderRequestsListView.as_view(), name='order_requests_list'),
    path('products/order/<int:pk>/state/', views.SetOrderRequestStatusView.as_view(), name='order_request_deliver'),
]
