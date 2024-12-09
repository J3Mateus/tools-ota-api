from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.device.serializers import DeviceListOutputSerializer, DeviceFilterSerializer
from apps.device.selectors import device_list
from apps.api.pagination import LimitOffsetPagination, get_paginated_response

class DeviceListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = DeviceListOutputSerializer
    filter_serializer = DeviceFilterSerializer

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Listar dispositivos",
        operation_description="Lista todos os dispositivos com filtros opcionais.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def get(self, request):
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        all_records = request.query_params.get("all")
        if all_records == "true":
            devices = device_list(filters=filters_serializer.validated_data)
            serializer = self.output_serializer(devices, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        devices = device_list(filters=filters_serializer.validated_data)
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=devices,
            request=request,
            view=self,
        )
