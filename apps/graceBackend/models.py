from django.db import models
from apps.authentication.models import User
from multiselectfield import MultiSelectField

class Entry(models.Model):
    MOOD_CHOICES = (
        ('Ecstatic', 'Ecstatic'),
        ('Happy', 'Happy'),
        ('Okay', 'Okay'),
        ('Anxious', 'Anxious'),
        ('Sad', 'Sad'),
    )
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    mood = MultiSelectField(choices = MOOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title