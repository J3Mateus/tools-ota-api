from django.urls import include, path
from apps.device.api import (
    DeviceCreateApi,
    DeviceListApi,
    DeviceUpdateApi,
    DeviceByIDApi,
    DeviceDeleteApi,
    DeviceGetFirmwareApi,
    DeviceGetCurrentVersionApi
)

urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("", DeviceListApi.as_view(), name="list_device"),
                    path("<uuid:uuid>/", DeviceByIDApi.as_view(), name="device_by_id"),
                    path("firmware/<str:device_id>/", DeviceGetFirmwareApi.as_view(), name="device_firmware"),
                    path("current_version/<str:device_id>/", DeviceGetCurrentVersionApi.as_view(), name="device_current_version"),
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
                    path("", DeviceCreateApi.as_view(), name="create_device"),
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
                    path("<uuid:uuid>/", DeviceUpdateApi.as_view(), name="update_device"),
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
                    path("<uuid:uuid>/", DeviceDeleteApi.as_view(), name="delete_device"),
                ],
                "delete",
            )
        ),
    ),
]
