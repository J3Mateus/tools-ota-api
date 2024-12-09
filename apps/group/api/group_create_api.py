from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.group.serializers import GroupCreateInputSerializer, GroupCreateOutputSerializer
from apps.group.services import group_create

class GroupCreateApi(APIView):
    input_serializer = GroupCreateInputSerializer
    output_serializer = GroupCreateOutputSerializer

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Criar um grupo",
        operation_description="Cria um novo grupo.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group = group_create(**serializer.validated_data)
        data = self.output_serializer(group).data
        return Response(status=status.HTTP_201_CREATED, data=data)
