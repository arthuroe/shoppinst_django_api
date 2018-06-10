from django.db import models

# Create your models here.


class ShoppingList(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class ShoppingListItem(models.Model):
    name = models.CharField(max_length=80)
    shoppinglist = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
