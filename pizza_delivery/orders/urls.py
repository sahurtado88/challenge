from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = "orders"

urlpatterns = [
    path("place_order/", views.place_order, name="place_order"),
    path("orders/", views.view_orders, name="orders"),

]