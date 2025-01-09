from rest_framework import serializers

from apps.files.serializers.output_serializer import FileOutputListSerializer

class FirmwareListOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()
    use_code = serializers.BooleanField()
    
class FirmwareCreateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()
    use_code = serializers.BooleanField()

class FirmwareUpdateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()
    use_code = serializers.BooleanField()

class FirmwareByIDOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()
    use_code = serializers.BooleanField()

class FirmwareByDeviceIDOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()
    use_code = serializers.BooleanField()

class FirmwareOutputDeleteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    code = serializers.CharField(allow_null=True)
    is_deleted = serializers.BooleanField()
    file = FileOutputListSerializer()
    use_code = serializers.BooleanField()
    

