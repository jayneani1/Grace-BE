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
    description = models.TextField(blank=True)
    mood = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.title