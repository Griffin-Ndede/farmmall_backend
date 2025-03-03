from django.db import models
from datetime import timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractUser

#user model
class User(AbstractUser):
    # Add any additional fields if needed
    pass

# Activity model to store activities (main and projections)
class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities')
    crop_name = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    activity_date = models.DateField()

    def __str__(self):
        return f"{self.crop_name} - {self.activity}"

    def save(self, *args, **kwargs):
        # When a new activity is saved, trigger projections if it's planting
        super().save(*args, **kwargs)
        if self.activity.lower() == 'planting':
            # Create projection activities for weeding and harvesting
            self.create_projection_activities()

    def create_projection_activities(self):
        """Create projection activities for weeding and harvesting."""
        # Create weeding and harvesting projections based on the activity date
        weeding_date = self.activity_date + timedelta(weeks=3)  # 3 weeks after planting
        harvesting_date = self.activity_date + timedelta(weeks=12)  # 12 weeks after planting

        # Create and save the projection activities
        Activity.objects.create(
            user=self.user,
            crop_name=self.crop_name,
            activity="Weeding",
            activity_date=weeding_date,
        )
        Activity.objects.create(
            user=self.user,
            crop_name=self.crop_name,
            activity="Harvesting",
            activity_date=harvesting_date,
        )