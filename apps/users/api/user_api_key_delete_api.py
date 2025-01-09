from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.users.serializers import UserApiKeyDeleteOutputSerializer
from apps.users.services import key_delete

from rest_framework.permissions import IsAuthenticated

from apps.users.selectors import user_get_login_data

class KeyDeleteApi(APIView):

    permission_classes = [IsAuthenticated]
    output_serializer = UserApiKeyDeleteOutputSerializer

    @swagger_auto_schema(
        tags=["User"],
        operation_summary="Excluir uma key",
        operation_description="Exclui uma key pelo UUID.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def delete(self, request, uuid):

        user = user_get_login_data(user=request.user)
        key = key_delete(uuid=uuid,user=user)
        data = self.output_serializer(key).data
        return Response(status=status.HTTP_200_OK, data=data)
