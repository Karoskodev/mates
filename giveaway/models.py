from django.db import models
from django.utils import timezone


class giveaway(models.Model):

    ANSWER = [
        ('Hikaru Nakamura', 'Hikaru Nakamura'),
        ('Magnus Carlsen', 'Magnus Carlsen'),
    ]

    answer = models.CharField(max_length=20, choices=ANSWER)
    rating = models.IntegerField(help_text="Chess rating (ELO rating)")
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email