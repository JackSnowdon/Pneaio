from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


@login_required
def world_index(request):
    profile = request.user.profile
    cards = Card.objects.filter(created_by=profile).order_by('-id')[:5]
    decks = Deck.objects.filter(owned_by=profile).order_by('-id')[:5]
    return render(request, "world_index.html", {"cards": cards, "decks": decks, "profile": profile})


# Cards


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
def view_card(request, pk):
    this_card = get_object_or_404(Card, pk=pk)
    star_levels = list(range(0, this_card.level))
    return render(request, "view_card.html", {"this_card": this_card, "star_levels": star_levels})


@login_required
def view_all_cards(request):
    cards = Card.objects.order_by('-id')
    return render(request, "view_all_cards.html", {"cards": cards})
    

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


# Deck

@login_required
def create_deck(request):
    if request.method == "POST":
        deck_form = NewDeckForm(request.POST)
        if deck_form.is_valid():
            form = deck_form.save(commit=False)
            form.owned_by = request.user.profile
            form.save()
            messages.error(request, "Created {0}".format(form.name), extra_tags="alert")
            return redirect("world_index")    
    else:
        deck_form = NewDeckForm()
    return render(request, "create_deck.html", {"deck_form": deck_form})


@login_required
def delete_deck(request, pk):
    this_deck = get_object_or_404(Deck, pk=pk)
    if this_deck.owned_by == request.user.profile:
        this_deck.delete()
        messages.error(
            request, f"Deleted {this_deck}", extra_tags="alert"
        )
        return redirect(reverse("world_index"))
    else:
        messages.error(request, f"Deck Not Yours To Delete", extra_tags="alert")
        return redirect("world_index")


@login_required
def deck(request, pk):
    this_deck = get_object_or_404(Deck, pk=pk)
    card_order = this_deck.cards.all().order_by('card__id')
    return render(request, "deck.html", {"this_deck": this_deck, "card_order": card_order})


@login_required
def add_single_card(request, pk):
    this_deck = get_object_or_404(Deck, pk=pk)
    cards = this_deck.cards.all()
    if cards.count() >= this_deck.size:
        messages.error(request, f"{this_deck} Has {this_deck.size} Cards Already", extra_tags="alert")
        return redirect("deck", this_deck.id)
    if request.method == "POST":
        add_form = AddCardToDeck(request.POST)
        if add_form.is_valid():
            form = add_form.save(commit=False)
            card_count = 0
            for card in cards:
                if card.card.id == form.card.id:
                    card_count += 1
                    if card_count == 3:
                        messages.error(request, f"{this_deck} Has 3 {form.card.name} Cards Already", extra_tags="alert")
                        return redirect("add_single_card", this_deck.id)
            form.deck = this_deck
            form.save()
            messages.error(request, f"Added {form.card.name} To {this_deck}", extra_tags="alert")
            return redirect("deck", this_deck.id)    
    else:
        add_form = AddCardToDeck()
    return render(request, "add_single_card.html", {"add_form": add_form, "this_deck": this_deck})


@login_required
def remove_single_card(request, pk):
    this_card = get_object_or_404(CardInstance, pk=pk)
    this_deck = this_card.deck
    this_card.delete()
    messages.error(request, f"Revmoed {this_card} From {this_deck}", extra_tags="alert")
    return redirect("deck", this_deck.id)

# Home Base

@login_required
def create_base(request):
    if request.method == "POST":
        base_form = NewBase(request.POST)
        if base_form.is_valid():
            form = base_form.save(commit=False)
            form.linked = request.user.profile
            form.save()
            messages.error(request, "New Base Created: {0}".format(form.name), extra_tags="alert")
            return redirect("world_index")    
    else:
        base_form = NewBase()
    return render(request, "create_base.html", {"base_form": base_form})

