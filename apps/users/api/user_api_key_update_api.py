from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.users.serializers import UserApiKeyUpdateInputSerializer, UserApiKeyByIdOutputSerializer
from apps.users.services import key_update
from utils import get_object
from apps.core.exceptions import NotFoundError, UpdateError
from apps.users.models import UserAPIKey
from rest_framework.permissions import IsAuthenticated

class KeyUpdateApi(APIView):
    input_serializer = UserApiKeyUpdateInputSerializer
    output_serializer = UserApiKeyByIdOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["User"],
        operation_summary="Atualizar uma api key",
        operation_description="Atualiza os dados de uma api key pelo UUID.",
        request_body=input_serializer,
        responses={status.HTTP_202_ACCEPTED: output_serializer},
    )
    def patch(self, request, uuid):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        key = get_object(UserAPIKey, id=uuid)
        if key is None:
            raise NotFoundError(extra={"uuid": uuid})
        new_key, updated = key_update(key=key, data=serializer.validated_data)
        if not updated:
            raise UpdateError(extra={"uuid": uuid}, status_code=status.HTTP_406_NOT_ACCEPTABLE)
        data = self.output_serializer(new_key).data
        return Response(status=status.HTTP_202_ACCEPTED, data=data)
