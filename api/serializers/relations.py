from rest_framework import serializers

import core.models as models


class CustomUserRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id", "username")
