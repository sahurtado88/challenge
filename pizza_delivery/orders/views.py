from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from .forms import PizzaOrderForm
from .models import PizzaOrder

def place_order(request):
    if request.method== "POST":
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/orders/orders/")
    else:
        form =PizzaOrderForm()    
    return render (
        request,
        "place_order.html",
        {"form": form}
    )

def view_orders(request):
    orders= PizzaOrder.objects.all()
    return render(request, 'orders_table.html', {'orders':orders})


