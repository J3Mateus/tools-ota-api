from rest_framework import serializers

class RolesSerializer(serializers.Serializer):
    id   = serializers.UUIDField()
    code = serializers.CharField()
    name = serializers.CharField()
    is_deleted  = serializers.BooleanField()