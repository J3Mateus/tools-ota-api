from rest_framework import serializers

from apps.files.serializers.output_serializer import FileOutputListSerializer

class FirmwareListOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    link_bin = serializers.URLField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()

class FirmwareCreateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    link_bin = serializers.URLField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()

class FirmwareUpdateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    link_bin = serializers.URLField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()

class FirmwareByIDOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    link_bin = serializers.URLField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()

class FirmwareByDeviceIDOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()

class FirmwareOutputDeleteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    link_bin = serializers.URLField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()

    

