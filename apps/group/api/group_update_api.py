from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.group.serializers import GroupUpdateInputSerializer, GroupUpdateOutputSerializer
from apps.group.services import group_update
from utils import get_object
from apps.core.exceptions import NotFoundError, UpdateError
from apps.group.models import Group

class GroupUpdateApi(APIView):
    input_serializer = GroupUpdateInputSerializer
    output_serializer = GroupUpdateOutputSerializer

    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Atualizar um grupo",
        operation_description="Atualiza os dados de um grupo pelo UUID.",
        request_body=input_serializer,
        responses={status.HTTP_202_ACCEPTED: output_serializer},
    )
    def patch(self, request, uuid):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group = get_object(Group, uuid=uuid)
        if group is None:
            raise NotFoundError(extra={"uuid": uuid})
        new_group, updated = group_update(group=group, data=serializer.validated_data)
        if not updated:
            raise UpdateError(extra={"uuid": uuid}, status_code=status.HTTP_406_NOT_ACCEPTABLE)
        data = self.output_serializer(new_group).data
        return Response(status=status.HTTP_202_ACCEPTED, data=data)
