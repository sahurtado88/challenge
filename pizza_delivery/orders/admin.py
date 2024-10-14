from django.contrib import admin
from .models import PizzaOrder

class OrdersAdmin(admin.ModelAdmin):
    list_display=("pizza_type", "comments")

admin.site.register(PizzaOrder, OrdersAdmin)