from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required
def world_index(request):
    cards = Card.objects.all()
    print(cards)
    return render(request, "world_index.html", {"cards": cards})


@login_required
def create_card(request):
    if request.method == "POST":
        card_form = NewCardForm(request.POST)
        if card_form.is_valid():
            form = card_form.save(commit=False)
            form.created_by = request.user.profile
            form.save()
            messages.error(request, "Started {0}".format(form.name), extra_tags="alert")
            return redirect("world_index")
    else:
        card_form = NewCardForm()
    return render(request, "create_card.html", {"card_form": card_form})