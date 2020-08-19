from django.urls import path
from .views import *

urlpatterns = [
    path('world_index/', world_index, name="world_index"),
    path('create_card/', create_card, name="create_card"),
    path(r'view_card/<int:pk>', view_card, name="view_card"),
    path('view_all_cards', view_all_cards, name="view_all_cards"),
    path(r'edit_card/<int:pk>', edit_card, name="edit_card"),
    path(r'delete_card/<int:pk>', delete_card, name="delete_card"),
    path('create_deck/', create_deck, name="create_deck"),
    path(r'delete_deck/<int:pk>', delete_deck, name="delete_deck"),
]