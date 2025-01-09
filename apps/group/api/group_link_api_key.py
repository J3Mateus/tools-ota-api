# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados ao Swagger
from drf_yasg.utils import swagger_auto_schema

# Imports dos Serializers e Services
from rest_framework.permissions import IsAuthenticated
from apps.group.services.group_link_api_key import group_link_api_key

from apps.group.serializers.output_serializer import GroupByIDOutputSerializer

class GroupLinkApiKeyApi(APIView):
    """Rota de criação de API key do usuário."""

    output_serializer = GroupByIDOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Vincular apikey ao grupo",
        operation_description="Vincula uma nova API key ao grupo.",
        request_body=None,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request , group_uuid , api_key_uuid):
        
        group = group_link_api_key(group_uuid=group_uuid,api_key_uuid=api_key_uuid)

        data = self.output_serializer(group).data
        return Response(status=status.HTTP_201_CREATED, data=data)