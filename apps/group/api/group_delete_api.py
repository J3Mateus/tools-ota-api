from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.group.serializers import GroupOutputDeleteSerializer
from apps.group.services import group_delete

class GroupDeleteApi(APIView):
    output_serializer = GroupOutputDeleteSerializer

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Excluir um grupo",
        operation_description="Exclui um grupo pelo UUID.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def delete(self, request, uuid):
        group = group_delete(uuid=uuid)
        data = self.output_serializer(group).data
        return Response(status=status.HTTP_200_OK, data=data)
