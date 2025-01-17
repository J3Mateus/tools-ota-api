from django.urls import include, path
from apps.device.api import (
    DeviceCreateApi,
    DeviceListApi,
    DeviceUpdateApi,
    DeviceByIDApi,
    DeviceDeleteApi,
    DeviceGetFirmwareApi,
    DeviceGetCurrentVersionApi,
    DeviceUpdateVersionCurrentApi,
    DeviceAddFirmwareApi,
    DeviceAddWifiApi,
    DeviceInitializeOtaApi,
    DeviceLinkApiKeyApi,
    DeviceForcedUpdateApi,
    DeviceRemoveFirmwareApi,
    DeviceStatusBuildApi
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
                    path("add-firmware/", DeviceAddFirmwareApi.as_view(), name="add_firmware"),
                    path("add-wifi/", DeviceAddWifiApi.as_view(), name="add_wifi"),
                    path("initialize-ota/<uuid:uuid>/", DeviceInitializeOtaApi.as_view(), name="initialize_ota"),
                    path("link/<str:device_id>/<str:firmware_id>/", DeviceUpdateVersionCurrentApi.as_view(), name="link_device"),
                    path("link-api-key/<uuid:device_uuid>/<uuid:api_key_uuid>/", DeviceLinkApiKeyApi.as_view(),name="link_api_key"),
                    path("forced-update/<uuid:uuid>/", DeviceForcedUpdateApi.as_view(), name="forced_update"),
                    path("remove-firmware/<uuid:uuid>/", DeviceRemoveFirmwareApi.as_view(), name="remove_firmware"),
                    path("status-build/", DeviceStatusBuildApi.as_view(), name="status_build"),
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
