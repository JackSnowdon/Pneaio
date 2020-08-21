from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from accounts.models import Profile

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=255)
    level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=0)
    attack = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], default=0)
    defense = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], default=0)
    speed = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], default=0)
    created_by = models.ForeignKey(Profile, related_name='creations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Base(models.Model):
    name = models.CharField(max_length=255)
    wins = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)], default=0)
    linked = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OwnedCard(models.Model):
    card = models.ForeignKey(Card, related_name='cards', on_delete=models.CASCADE)
    base = models.ForeignKey(Base, related_name='library', on_delete=models.CASCADE)

    def __str__(self):
        return self.card.name


class Deck(models.Model):
    name = models.CharField(max_length=255)
    size = models.PositiveIntegerField(validators=[MinValueValidator(20), MaxValueValidator(100)], default=20)
    owned_by = models.ForeignKey(Base, related_name='decks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CardInstance(models.Model):
    card = models.ForeignKey(OwnedCard, related_name='indecks', on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, related_name='cards', on_delete=models.CASCADE)

    def __str__(self):
        return self.card.name