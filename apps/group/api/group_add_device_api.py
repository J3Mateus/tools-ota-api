from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from apps.group.serializers import GroupAddDeviceOutputSerializer ,GroupAddDeviceInputSerializer
from apps.group.services import group_add_device
from apps.users.selectors import user_get_login_data

class GroupAddDeviceApi(APIView):

    permission_classes = [IsAuthenticated]

    input_serializer = GroupAddDeviceInputSerializer
    output_serializer = GroupAddDeviceOutputSerializer

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Vincular dispositivo em um grupo",
        operation_description="Vincular dispositivo em um grupo.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        group = group_add_device(**serializer.validated_data)
        data = self.output_serializer(group).data
        return Response(status=status.HTTP_201_CREATED, data=data)