from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Family(models.Model):
    None

class FamilyMember(User):

    family = models.ForeignKey(Family, on_delete=models.RESTRICT, related_name='members', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Family Members"  # Change "Tasks" to "Task Items"