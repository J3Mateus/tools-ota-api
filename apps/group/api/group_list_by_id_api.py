from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.group.serializers import GroupByIDOutputSerializer
from apps.group.selectors import group_list_by_id
from rest_framework.permissions import IsAuthenticated

class GroupByIDApi(APIView):
    output_serializer = GroupByIDOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Buscar um grupo",
        operation_description="Busca um grupo específico pelo UUID.",
        responses={status.HTTP_200_OK: output_serializer},
        
    )
    def get(self, request, uuid):
        group = group_list_by_id(uuid=uuid)
        data = self.output_serializer(group).data
        return Response(status=status.HTTP_200_OK, data=data)
