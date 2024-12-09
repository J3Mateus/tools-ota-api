from rest_framework import serializers

class WifiListOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    SSDI = serializers.CharField()
    password = serializers.CharField()
    is_deleted = serializers.BooleanField()

class WifiCreateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    SSDI = serializers.CharField()
    password = serializers.CharField()
    is_deleted = serializers.BooleanField()

class WifiUpdateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    SSDI = serializers.CharField()
    password = serializers.CharField()
    is_deleted = serializers.BooleanField()

class WifiByIDOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    SSDI = serializers.CharField()
    password = serializers.CharField()
    is_deleted = serializers.BooleanField()

class WifiOutputDeleteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    SSDI = serializers.CharField()
    password = serializers.CharField()
    is_deleted = serializers.BooleanField()
