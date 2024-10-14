from . import models
from django.forms import ModelForm

class PizzaOrderForm(ModelForm):
    class Meta:
        model= models.PizzaOrder
        fields=['pizza_type', 'comments']