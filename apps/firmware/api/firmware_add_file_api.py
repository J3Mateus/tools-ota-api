# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#Imports relacionados ao Swagger
from drf_yasg.utils import swagger_auto_schema

#Imports dos Serializers e Services
from apps.firmware.services import firmware_add_file
from apps.files.serializers import FileCreateInputSerializer
from apps.firmware.serializers import FirmwareByIDOutputSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey


class FirmwareAddFileApi(APIView):
    """Adiciona arquivo em firmware"""
    input_serializer = FileCreateInputSerializer
    output_serializer = FirmwareByIDOutputSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
        
    @swagger_auto_schema(
        tags=["Firmware"],
        operation_summary="Adicionar arquivo em firmware",
        operation_description="Adiciona arquivo em firmware.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )

    def post(self, request,uuid):

        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        firmware = firmware_add_file(firmware_id=uuid, file=serializer.validated_data['file'])

        data = self.output_serializer(firmware).data

        return Response(status=status.HTTP_201_CREATED,data=data)