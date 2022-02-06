from sre_constants import CATEGORY
from django.db import models

CATEGORY_CHOICES = (
    'ux', 'dev', 'design', 'marketing', 'other'
)


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.TextChoices('category', CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
