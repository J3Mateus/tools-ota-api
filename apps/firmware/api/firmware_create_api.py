from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.firmware.serializers import FirmwareCreateInputSerializer, FirmwareCreateOutputSerializer
from apps.firmware.services import firmware_create
from rest_framework.permissions import IsAuthenticated

from apps.users.selectors import user_get_login_data

class FirmwareCreateApi(APIView):
    input_serializer = FirmwareCreateInputSerializer
    output_serializer = FirmwareCreateOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Firmware"],
        operation_summary="Criar um firmware",
        operation_description="Cria um novo firmware.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = user_get_login_data(user=request.user)

        firmware = firmware_create(**serializer.validated_data,user=user)
        data = self.output_serializer(firmware).data
        return Response(status=status.HTTP_201_CREATED, data=data)
