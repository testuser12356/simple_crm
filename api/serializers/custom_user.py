from rest_framework import serializers

import core.models as models


class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id", "username", "password", "first_name", "last_name")


class GetCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = (
            "id", "username", "first_name",
            "last_name", "date_joined"
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["date_joined"] = instance.date_joined.strftime("%Y-%m-%d %H:%M")
        return data
