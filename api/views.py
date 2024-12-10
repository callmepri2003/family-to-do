from rest_framework.decorators import action
from familyMembers.models import FamilyMember
from familyMembers.serializers import FamilyMemberSerializer, UserSerializer
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally filter tasks by a `username` query parameter.
        """
        username = self.request.query_params.get('username', None)
        if username:
            family_member_model = FamilyMember.objects.get(username=username)  # Retrieve the User model (FamilyMember in this case)
            family_member = FamilyMember.objects.filter(username=username).first()
            if family_member:
                return self.queryset.filter(assigned_to=family_member)  # Replace `assigned_to` with the actual task field
            else:
                return self.queryset.none()
        return self.queryset

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

    @action(detail=False, methods=['GET'])
    def getAllTasks():
        return 

class LoginAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"Success": "Login Successful", "User": request.user.username, "userId": request.user.id}, status=status.HTTP_200_OK)