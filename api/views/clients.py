from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

import core.models as models
import api.serializers as serializer


class ClientAPIView(ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializer.ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)
