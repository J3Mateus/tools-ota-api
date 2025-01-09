from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from apps.group.serializers import GroupRemoveDeviceOutputSerializer ,GroupRemoveDeviceInputSerializer
from apps.group.services import group_remove_device
from apps.users.selectors import user_get_login_data

class GroupRemoveDeviceApi(APIView):

    permission_classes = [IsAuthenticated]

    input_serializer = GroupRemoveDeviceInputSerializer
    output_serializer = GroupRemoveDeviceOutputSerializer

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Remove dispositivo de um grupo",
        operation_description="Remove dispositivo de um grupo",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def delete(self, request,group_uuid,device_uuid):

        group = group_remove_device(device_id=device_uuid,group_id=group_uuid)
        data = self.output_serializer(group).data
        return Response(status=status.HTTP_201_CREATED, data=data)