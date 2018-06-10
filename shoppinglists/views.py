from django.shortcuts import render
from rest_framework import viewsets
from .models import ShoppingList, ShoppingListItem
from .serializer import ShoppingListSerializer, ShoppingListItemSerializer


class ShoppingListView(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ShoppingListItemView(viewsets.ModelViewSet):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer
