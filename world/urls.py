from django.urls import path
from .views import *

urlpatterns = [
    path('world_index/', world_index, name="world_index"),
    path('create_card/', create_card, name="create_card"),
]