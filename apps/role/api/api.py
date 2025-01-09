# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados à autenticação da API
from apps.api.mixins import ApiAuthMixin

# Imports relacionados à paginação da API
from apps.api.pagination import LimitOffsetPagination, get_paginated_response
from apps.docs.role.response import RESPONSE_ROLE_LIST

# Imports relacionados aos papéis (roles)
from apps.role.selectors.selector import role_list
from apps.role.serializers.filter_serializer import RoleFilterSerializer
from apps.role.serializers.output_serializer import RolesSerializer
# Imports do drf-yasg (geração de documentação Swagger)
from drf_yasg.utils import swagger_auto_schema

class RolesListApi(ApiAuthMixin,APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = RolesSerializer
    filter_serializer = RoleFilterSerializer
    @swagger_auto_schema(
        operation_summary="Listar Roles",
        operation_description="Esta rota permite listar as roles com os filtros fornecidos. As roles serão retornadas de acordo com os filtros aplicados.",
        responses=RESPONSE_ROLE_LIST,
    )
    def get(self, request):
        
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        all =  request.query_params.get("all")
        if all == 'true':
            # Se o parâmetro 'all' estiver presente, retorne todos os registros sem paginar
            roles = role_list(filters=filters_serializer.validated_data)
            serializer = self.output_serializer(roles, many=True)
            return Response(serializer.data)
        
        roles = role_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=roles,
            request=request,
            view=self,
        )
