from django.db import models
from django.utils import timezone

class PizzaOrder(models.Model):
    PIZZA_TYPES =[
        ('Vegetarian', 'Vegetarian'),
        ('Pepperoni', 'Pepperoni'),
        ('Roman Pizza', 'Roman Pizza'),
        ('Sicilian','Sicilian'),
        ('Hawaiian','Hawaiian'),
    ]
    pizza_type= models.CharField(max_length=20, choices=PIZZA_TYPES)
    comments= models.TextField(blank=True)

    def __str__(self):
        return f'{self.pizza_type} - {self.comments[:20]}'
