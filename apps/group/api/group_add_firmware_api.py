from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.group.serializers import GroupAddFirmwareInputSerializer, GroupAddFirmwareOutputSerializer
from apps.group.services import group_add_firmware

class GroupAddFirmwareApi(APIView):
    input_serializer = GroupAddFirmwareInputSerializer
    output_serializer = GroupAddFirmwareOutputSerializer

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Vincular firmware em um grupo",
        operation_description="Vincular firmware em um grupo.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group = group_add_firmware(**serializer.validated_data)
        data = self.output_serializer(group).data
        return Response(status=status.HTTP_201_CREATED, data=data)
