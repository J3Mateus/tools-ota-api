# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados ao Swagger
from drf_yasg.utils import swagger_auto_schema

# Imports dos Serializers e Services
from rest_framework.permissions import IsAuthenticated
from apps.api.pagination import LimitOffsetPagination, get_paginated_response
from apps.users.selectors.user_get_login_data import user_get_login_data
from apps.users.selectors.user_get_api_key import user_get_list_api_key
from apps.users.serializers.output_serializer import UserApiKeyOutputSerializer

class UserListApiKeyApi(APIView):
    """Rota para buscar api key"""
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = UserApiKeyOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["User"],
        operation_summary="Buscar lista de api key",
        operation_description="Busca as api key vinculada ao usuario",
        request_body=None,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def get(self, request):

        user = user_get_login_data(user=request.user)
        all_records = request.query_params.get("all")

        if all_records == "true":
            api_key = user_get_list_api_key(user_id=user.id)
            serializer = self.output_serializer(api_key, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        api_key = user_get_list_api_key(user_id=user.id)
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=api_key,
            request=request,
            view=self,
        )
