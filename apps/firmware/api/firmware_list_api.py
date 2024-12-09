from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.firmware.serializers.output_serializer import FirmwareListOutputSerializer
from apps.firmware.serializers.filter_serializer import FirmwareFilterSerializer
from apps.firmware.selectors import firmware_list
from apps.api.pagination import LimitOffsetPagination, get_paginated_response

class FirmwareListApi(APIView):
    """
    API para listar todos os firmwares com filtros opcionais.
    """
    class Pagination(LimitOffsetPagination):
        default_limit = 20

    output_serializer = FirmwareListOutputSerializer
    filter_serializer = FirmwareFilterSerializer

    @swagger_auto_schema(
        tags=["Firmware"],
        operation_summary="Listar firmwares",
        operation_description="Lista todos os firmwares com filtros opcionais.",
        responses={status.HTTP_200_OK: output_serializer},
        
    )
    def get(self, request):
        filters_serializer = self.filter_serializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        all_records = request.query_params.get("all")
        if all_records == "true":
            firmwares = firmware_list(filters=filters_serializer.validated_data)
            serializer = self.output_serializer(firmwares, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        firmwares = firmware_list(filters=filters_serializer.validated_data)
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.output_serializer,
            queryset=firmwares,
            request=request,
            view=self,
        )
