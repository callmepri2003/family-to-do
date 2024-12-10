from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Family(models.Model):
    None

class FamilyMember(User):
    family = models.ForeignKey(Family, on_delete=models.RESTRICT, related_name='members', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Family Members"

    def save(self, *args, **kwargs):
        # Check if password is set and hash it if necessary
        if self.password and not self.password.startswith('$'):  # If password is not already hashed
            self.set_password(self.password)  # Use Django's built-in method to hash the password
        super(FamilyMember, self).save(*args, **kwargs)  # Call the original save method
