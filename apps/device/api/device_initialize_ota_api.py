from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.api.mixins import ApiAuthMixin
from apps.device.serializers import DeviceByIDOutputSerializer
from apps.device.services import device_initialize_ota

from rest_framework.permissions import IsAuthenticated

class DeviceInitializeOtaApi(ApiAuthMixin,APIView):

    output_serializer = DeviceByIDOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Iniciazaliza o OTA de um device",
        operation_description="Inicializa o processo de atualização em um device.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def post(self, request, uuid):
        device = device_initialize_ota(uuid=uuid)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_200_OK, data=data)
