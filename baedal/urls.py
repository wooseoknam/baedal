from django.urls import path

from . import views

app_name = 'baedal'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:store_id>/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart')
]