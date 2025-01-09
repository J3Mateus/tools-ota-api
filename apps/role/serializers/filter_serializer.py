from rest_framework import serializers

class RoleFilterSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)    
    is_deleted  = serializers.BooleanField(required=False)