from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from tasks.models import Task
from tasks.models import Status as taskStatus
from familyMembers.models import Family, FamilyMember


# Create your tests here.

class APITests(APITestCase):

    def setUp(self):
        family = Family.objects.create()
        self.familyMember1 = FamilyMember(username='user1', password='testpassword1', family=family)
        self.familyMember2 = FamilyMember(username='user2', password='testpassword2', family=family)
        self.familyMember1.save()
        self.familyMember2.save()
        self.client.force_authenticate(user=self.familyMember1)
    
    def testAssignTask(self):
        url = reverse('task-assign-task')
        data = {
            "title": "Assign Test",
            "description": "This is a pending task.",
            "status": 'PE',
            "assigned_to": self.familyMember2.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Assign Test')
    
    def testRejectTask(self):
        originalTask = Task(title='Do this!', assigned_to=self.familyMember1)
        originalTask.save()

        url = reverse('task-reject-task', args=([originalTask.pk]))
        response = self.client.get(url, {}, format='json')

        updatedTask = Task.objects.get(pk=originalTask.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updatedTask.getStatus(), taskStatus.REJECTED)

    def testAcceptTask(self):
        originalTask = Task(title='Do this!', assigned_to=self.familyMember1)
        originalTask.save()

        url = reverse('task-accept-task', args=([originalTask.pk]))
        response = self.client.get(url, {}, format='json')

        updatedTask = Task.objects.get(pk=originalTask.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updatedTask.getStatus(), taskStatus.ACCEPTED)
    
    def testCompleteTask(self):
        originalTask = Task(title='Do this!', assigned_to=self.familyMember1)
        originalTask.save()

        url = reverse('task-complete-task', args=([originalTask.pk]))
        response = self.client.get(url, {}, format='json')

        updatedTask = Task.objects.get(pk=originalTask.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updatedTask.getStatus(), taskStatus.COMPLETED)
        
