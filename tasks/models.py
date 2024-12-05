from django.db import models
from familyMembers.models import FamilyMember
from django.utils.translation import gettext_lazy as _


class Status(models.TextChoices):
    COMPLETED = "CO", _("Completed")
    ACCEPTED = "AC", _("Accepted")
    PENDING = "PE", _("Pending")
    REJECTED = "RE", _("Rejected")
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=Status, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def rejectTask(self):
        self.status = "RE"
        self.save()
    
    def acceptTask(self):
        self.status = "AC"
        self.save()
    
    def completeTask(self):
        self.status = "CO"
        self.save()
    
    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def __str__(self):
        return self.title
