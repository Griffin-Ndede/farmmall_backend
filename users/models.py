from django.db import models

# User model
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# PotatoCrop model
class PotatoCrop(models.Model):
    activity = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)  # Optional field
    county = models.CharField(max_length=100)
    fertilizer_type = models.CharField(max_length=100, null=True, blank=True)  # Optional field
    irrigation_used = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)  # Optional field

    def __str__(self):
        return f"Potato Crop in {self.county} planted on {self.activity}"

class Activity(models.Model):
    crop_name = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    activity_date = models.DateField()

    def __str__(self):
        return f"{self.crop_name} - {self.activity}"