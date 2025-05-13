from rest_framework import serializers

import core.models as models
from api.serializers.relations import CustomUserRelationSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        exclude = ("created_by", "status")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["status"] = instance.status
        data["deadline"] = instance.deadline.strftime("%Y-%m-%d %H:%M")
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        data["created_by"] = CustomUserRelationSerializer(instance.created_by).data
        data["assigned_to"] = CustomUserRelationSerializer(instance.assigned_to).data
        return data
