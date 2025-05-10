from rest_framework.viewsets import ModelViewSet

import core.models as models
import api.serializers as serializer


class TaskAPIView(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializer.TaskSerializer
