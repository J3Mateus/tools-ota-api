from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.api.mixins import ApiAuthMixin
from apps.group.serializers import GroupListOutputSerializer, GroupFilterSerializer
from apps.group.selectors import group_list
from apps.api.pagination import LimitOffsetPagination, get_paginated_response
from rest_framework.permissions import IsAuthenticated

from apps.users.selectors import user_get_login_data

class GroupListApi(ApiAuthMixin,APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = GroupListOutputSerializer
    filter_serializer = GroupFilterSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        tags=["Group"],
        operation_summary="Listar grupos",
        operation_description="Lista todos os grupos com filtros opcionais.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def get(self, request):
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        user = user_get_login_data(user=request.user)
        
        all_records = request.query_params.get("all")
        if all_records == "true":
            groups = group_list(filters=filters_serializer.validated_data,user=user)
            serializer = self.output_serializer(groups, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        groups = group_list(filters=filters_serializer.validated_data,user=user)
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=groups,
            request=request,
            view=self,
        )
