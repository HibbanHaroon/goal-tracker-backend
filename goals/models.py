from django.db import models
from django.conf import settings

class Goal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='goals'
    )
    text = models.TextField()
    order = models.FloatField()  # Using float for easier reordering
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        db_table = 'goals'

    def __str__(self):
        return f"{self.text[:50]}..."
