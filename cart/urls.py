from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cart-home'),
    path('add/', views.ItemsAddView.as_view(), name="add-item"),
    path('cartitems/', views.DisplayItems, name="cart-items"),
    path('add/cartitems/<int:pk>/delete/', views.ItemDeleteView.as_view(), name="item-delete"),
    path('add/cartitems/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
]
