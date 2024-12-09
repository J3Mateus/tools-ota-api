from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.device.serializers import DeviceByIDOutputSerializer
from apps.device.selectors import device_list_by_id

class DeviceByIDApi(APIView):
    output_serializer = DeviceByIDOutputSerializer

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Buscar um dispositivo",
        operation_description="Busca um dispositivo específico pelo ID.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def get(self, request, uuid):
        device = device_list_by_id(id=uuid)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_200_OK, data=data)
