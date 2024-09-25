from django.db import models

class PotatoCrop(models.Model):
    planting_date = models.DateField()
    region = models.CharField(max_length=100)
    fertilizer_type = models.CharField(max_length=100, null=True, blank=True)
    irrigation_used = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Potato Crop in {self.region} planted on {self.planting_date}"
