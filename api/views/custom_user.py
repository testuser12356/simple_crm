from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated

import core.models as models
import api.serializers as serializer


class CreateCustomUserView(CreateModelMixin, GenericViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.CreateCustomUserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.get("password")
        user = serializer.save()
        user.set_password(password)
        user.save()


class GetMe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user:
            data = serializer.GetCustomUserSerializer(request.user)
            return Response(data.data)
