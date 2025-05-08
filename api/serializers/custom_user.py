from rest_framework import serializers

import core.models as models


class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id", "username", "password", "first_name", "last_name")
