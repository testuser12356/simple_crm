from rest_framework import serializers

import core.models as models
import api.serializers.relations as relation


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        exclude = ("created_by",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        data["created_by"] = relation.CustomUserRelationSerializer(instance.created_by).data
        return data
