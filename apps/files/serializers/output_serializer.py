from rest_framework import serializers
from apps.files.models import File
from django.conf import settings

class FileOutputListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    type = serializers.CharField()
    file = serializers.SerializerMethodField()

    def get_file(self,obj:File):
        return f"{settings.TOOLS_OTA['domain']['base_url']}{obj.file.url}"
    