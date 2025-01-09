from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.api.mixins import ApiAuthMixin
from apps.group.serializers import GroupByIDOutputSerializer
from apps.group.services import group_initialize_ota

from rest_framework.permissions import IsAuthenticated

class GroupInitializeOtaApi(ApiAuthMixin,APIView):

    output_serializer = GroupByIDOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Iniciazaliza o OTA de um grupo",
        operation_description="Inicializa o processo de atualização em todos os dispositivos.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def post(self, request, uuid):
        group = group_initialize_ota(uuid=uuid)
        data = self.output_serializer(group).data
        return Response(status=status.HTTP_200_OK, data=data)
