from rest_framework import serializers

class RolesOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    code = serializers.CharField()

class UserOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    full_name  = serializers.CharField(required=False)
    email      = serializers.CharField(required=False)
    phone      = serializers.CharField(required=False)
    whatsapp   = serializers.CharField(required=False)
    is_deleted = serializers.BooleanField(required=False)
    roles      = serializers.SerializerMethodField(required=False)
    
    def get_roles(self,obj):
        roles = obj.roles.all()
        return RolesOutputSerializer(roles,many=True).data
    
class UserApiKeyOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    user = UserOutputSerializer()
    key = serializers.UUIDField()
    revoked_at = serializers.DateTimeField()

class UserApiKeyByIdOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    user = UserOutputSerializer()
    key = serializers.UUIDField()
    revoked_at = serializers.DateTimeField()

class UserApiKeyDeleteOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    user = UserOutputSerializer()
    key = serializers.UUIDField()
    revoked_at = serializers.DateTimeField()
    is_deleted = serializers.BooleanField()