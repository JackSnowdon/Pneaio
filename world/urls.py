from django.urls import path
from .views import *

urlpatterns = [
    path('world_index/', world_index, name="world_index"),
    path('create_card/', create_card, name="create_card"),
    path(r'edit_card/<int:pk>', edit_card, name="edit_card"),
    path(r'delete_card/<int:pk>', delete_card, name="delete_card"),
]