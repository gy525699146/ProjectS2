from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('detail/<slug:pk>', views.Detail.as_view(), name='detail'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('addcart/', views.AddCart.as_view(), name='addcart'),
    path('check/', views.Check.as_view(), name='check'),
]
