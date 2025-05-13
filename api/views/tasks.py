from rest_framework.viewsets import ModelViewSet

import core.models as models
import api.serializers as serializer
import utils.permissions as permissions


class TaskAPIView(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializer.TaskSerializer
    permission_classes = [permissions.ManagerPermission]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)

    def get_queryset(self):
        user = self.request.user
        tasks = super().get_queryset().filter(assigned_to=user)
        return tasks
