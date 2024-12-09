from rest_framework import serializers

class FileCreateInputSerializer(serializers.Serializer):
    file = serializers.FileField()
    file_url = serializers.URLField(required=False, allow_null=True)
