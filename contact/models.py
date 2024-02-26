from django.db import models
from django.utils import timezone

class contact(models.Model):

    SUBJECT = [
        ('Payment', 'Payment'),
        ('Order', 'Order'),
        ('Account', 'Account'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other'),
    ]

    subject = models.CharField(max_length=20, choices=SUBJECT)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email