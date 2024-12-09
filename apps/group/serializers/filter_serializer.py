from rest_framework import serializers

class GroupFilterSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    is_deleted = serializers.BooleanField(required=False)
    # active = serializers.BooleanField(required=False,allow_null=True)
