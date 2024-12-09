from django.urls import include, path
from apps.firmware.api import (
    FirmwareCreateApi,
    FirmwareListApi,
    FirmwareUpdateApi,
    FirmwareByIDApi,
    FirmwareDeleteApi,
    FirmwareAddFileApi
)

urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("", FirmwareListApi.as_view(), name="list_firmware"),
                    path("<uuid:uuid>/", FirmwareByIDApi.as_view(), name="firmware_by_id"),
                ],
                "get",
            )
        ),
    ),
    path(
        "create/",
        include(
            (
                [
                    path("", FirmwareCreateApi.as_view(), name="create_firmware"),
                    path("file/<uuid:uuid>", FirmwareAddFileApi.as_view(), name="add_file"),
                ],
                "create",
            )
        ),
    ),
    path(
        "update/",
        include(
            (
                [
                    path("<uuid:uuid>/", FirmwareUpdateApi.as_view(), name="update_firmware"),
                ],
                "update",
            )
        ),
    ),
    path(
        "delete/",
        include(
            (
                [
                    path("<uuid:uuid>/", FirmwareDeleteApi.as_view(), name="delete_firmware"),
                ],
                "delete",
            )
        ),
    ),
]
