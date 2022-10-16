from django.db import models
from authentication.models import User

# Create your models here.

class CardStack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    first_language = models.CharField(max_length=2)
    target_language = models.CharField(max_length=2)


class Card(models.Model):
    is_target_language = models.BooleanField()
    target_card = models.IntegerField(blank=True, null=True)
    card_stack = models.ForeignKey(CardStack, on_delete=models.CASCADE)
