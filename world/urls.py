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
    path(r'deck/<int:pk>', deck, name="deck"),
    path(r'add_single_card/<int:pk>', add_single_card, name="add_single_card"),
    path(r'remove_single_card/<int:pk>', remove_single_card, name="remove_single_card"),
    path('create_base/', create_base, name="create_base"),
    path(r'rename_base/<int:pk>', rename_base, name="rename_base"),
    path(r'delete_base/<int:pk>', delete_base, name="delete_base"),
    path(r'buy_card/<int:pk>', buy_card, name="buy_card"),
    path(r'base_library/<int:pk>', base_library, name="base_library"),
    path(r'sell_card/<int:pk>', sell_card, name="sell_card"),
]