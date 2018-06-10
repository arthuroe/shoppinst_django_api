from rest_framework import serializers
from .models import ShoppingList, ShoppingListItem


class ShoppingListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('id', 'name', 'description', 'url')


class ShoppingListItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = ('id', 'name', 'shoppinglist')
