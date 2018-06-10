from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('shoppinglists', views.ShoppingListView)
router.register('shoppinglist-item', views.ShoppingListItemView)

urlpatterns = [
    path('', include(router.urls)),
]
