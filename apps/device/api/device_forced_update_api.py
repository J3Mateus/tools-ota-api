from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.device.serializers import DeviceGetCurrentVersionOutputSerializer
from apps.device.services import device_forced_update
from rest_framework.permissions import IsAuthenticated

class DeviceForcedUpdateApi(APIView):
    output_serializer = DeviceGetCurrentVersionOutputSerializer
    permission_classes = [IsAuthenticated] 
    
    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Força a atualização de um dispostivo",
        operation_description="Foraça a atualização de um dispostivo em especifico.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def post(self, request, uuid):
        device = device_forced_update(device_id=uuid)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_200_OK, data=data)
