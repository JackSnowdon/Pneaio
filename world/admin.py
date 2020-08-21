from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Card)
admin.site.register(Base)
admin.site.register(OwnedCard)
admin.site.register(Deck)
admin.site.register(CardInstance)