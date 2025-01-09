from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.users.serializers import UserApiKeyByIdOutputSerializer
from apps.users.selectors import key_list_by_id
from rest_framework.permissions import IsAuthenticated

class KeyByIDApi(APIView):
    output_serializer = UserApiKeyByIdOutputSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        tags=["User"],
        operation_summary="Buscar uma key",
        operation_description="Busca uma key específica pelo ID.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def get(self, request, uuid):
        key = key_list_by_id(id=uuid)
        data = self.output_serializer(key).data
        return Response(status=status.HTTP_200_OK, data=data)
