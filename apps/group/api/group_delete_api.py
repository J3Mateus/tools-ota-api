from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.group.serializers import GroupOutputDeleteSerializer
from apps.group.services import group_delete

from rest_framework.permissions import IsAuthenticated

from apps.users.selectors import user_get_login_data

class GroupDeleteApi(APIView):

    permission_classes = [IsAuthenticated]
    output_serializer = GroupOutputDeleteSerializer

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Excluir um grupo",
        operation_description="Exclui um grupo pelo UUID.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def delete(self, request, uuid):

        user = user_get_login_data(user=request.user)
        group = group_delete(uuid=uuid,user=user)
        data = self.output_serializer(group).data
        return Response(status=status.HTTP_200_OK, data=data)
