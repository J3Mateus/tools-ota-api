# Imports do Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.api.mixins import ApiAuthMixin
from apps.api.pagination import LimitOffsetPagination, get_paginated_response
from rest_framework.permissions import IsAuthenticated
from apps.users.selectors import user_get_login_data
from apps.wifi.selectors import wifi_list

from apps.wifi.serializers import WifiListOutputSerializer, WifiFilterSerializer

from drf_yasg.utils import swagger_auto_schema


class WifiListApi(ApiAuthMixin,APIView):
    permission_classes = [IsAuthenticated]

    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = WifiListOutputSerializer
    filter_serializer = WifiFilterSerializer

    @swagger_auto_schema(
        tags=["Wifi"],
        operation_summary="Listar redes Wifi",
        operation_description="Lista as redes Wifi com suporte a paginação e filtros.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def get(self, request):
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        user = user_get_login_data(user=request.user)
        
        all_records = request.query_params.get("all")
        if all_records == 'true':
            # Se o parâmetro 'all' estiver presente, retorna todos os registros sem paginação
            wifi = wifi_list(filters=filters_serializer.validated_data,user=user)
            serializer = self.output_serializer(wifi, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        wifi = wifi_list(filters=filters_serializer.validated_data,user=user)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=wifi,
            request=request,
            view=self,
        )
