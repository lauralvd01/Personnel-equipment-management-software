from django.db import models

# Create your models here.

# Model creation with its fields
# Add as many models/fields as necessary.
class Motor(models.Model):
    n_serie = models.CharField(max_length=256)

