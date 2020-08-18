from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

@login_required
def world_index(request):
    cards = Card.objects.order_by('-id')[:5]
    return render(request, "world_index.html", {"cards": cards})


@login_required
def create_card(request):
    if request.method == "POST":
        card_form = NewCardForm(request.POST)
        if card_form.is_valid():
            form = card_form.save(commit=False)
            form.created_by = request.user.profile
            if card_limiter(request, form):
                form.save()
                messages.error(request, "Created {0}".format(form.name), extra_tags="alert")
                return redirect("world_index")    
    else:
        card_form = NewCardForm()
    return render(request, "create_card.html", {"card_form": card_form})


@login_required
def edit_card(request, pk):
    this_card = get_object_or_404(Card, pk=pk)
    profile = request.user.profile
    if profile == this_card.created_by or profile.staff_access:
        if request.method == "POST":
            card_form = NewCardForm(request.POST, instance=this_card)
            if card_form.is_valid():
                form = card_form.save(commit=False)
                if card_limiter(request, form):
                    form.save()
                    messages.error(request, "Edited {0}".format(form.name), extra_tags="alert")
                    return redirect("world_index")      
        else:
            card_form = NewCardForm(instance=this_card)
        return render(request, "edit_card.html", {"card_form": card_form, "this_card": this_card})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("world_index")


@login_required
def delete_card(request, pk):
    this_card = get_object_or_404(Card, pk=pk)
    if this_card.created_by == request.user.profile:
        this_card.delete()
        messages.error(
            request, f"Deleted {this_card}", extra_tags="alert"
        )
        return redirect(reverse("world_index"))
    else:
        messages.error(request, f"Card Not Yours To Delete", extra_tags="alert")
        return redirect("world_index")


# Card Helper Functions

def card_limiter(r, card):
    point_limit = card.level * 1750
    point_total = card.attack + card.defense + card.speed
    if point_total <= point_limit:
        return True
    else:
        messages.error(r, f"Point Total ({point_total}) Exceeds Limit ({point_limit})", extra_tags="alert")
        return False