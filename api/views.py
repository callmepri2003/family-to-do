from rest_framework.decorators import action
from familyMembers.models import FamilyMember
from familyMembers.serializers import FamilyMemberSerializer, UserSerializer
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.conf import settings

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def assign_task(self, request, pk=None):
        return self.create(request)
    
    @action(detail=True, methods=['GET'])
    def reject_task(self, request, pk=None):
        task = self.get_object()
        task.rejectTask()
        return Response({'status': 'Task rejected'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def accept_task(self, request, pk=None):
        task = self.get_object()
        task.acceptTask()
        return Response({'status': 'Task Accepted'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def complete_task(self, request, pk=None):
        task = self.get_object()
        task.completeTask()
        return Response({'status': 'Task Completed'}, status=status.HTTP_200_OK)


class FamilyMemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for simplicity
class MigrateView(View):
    def post(self, request, *args, **kwargs):
        try:
            # Execute the migrate command directly
            call_command('migrate', interactive=False)
            return JsonResponse({'status': 'success', 'message': 'Migrations applied successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)}, status=500)