from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from accounts.models import Profile

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=255)
    level = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    attack = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], default=0)
    defense = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], default=0)
    speed = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], default=0)
    created_by = models.ForeignKey(Profile, related_name='creations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
