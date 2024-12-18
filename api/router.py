from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'familyMembers', views.FamilyMemberViewSet)
router.register(r'users', views.UserViewSet)
