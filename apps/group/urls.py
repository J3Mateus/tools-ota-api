from django.urls import include, path
from apps.group.api import (
    GroupCreateApi,
    GroupListApi,
    GroupUpdateApi,
    GroupByIDApi,
    GroupDeleteApi,
    GroupAddFirmwareApi,
    GroupAddDeviceApi,
    GroupAddWifiApi,
    GroupInitializeOtaApi,
    GroupLinkApiKeyApi,
    GroupRemoveDeviceApi
)


urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("", GroupListApi.as_view(), name="list_group"),
                    path("<uuid:uuid>/", GroupByIDApi.as_view(), name="group_by_id"),
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
                    path("", GroupCreateApi.as_view(), name="create_group"),
                    path("add-firmware/", GroupAddFirmwareApi.as_view(), name="add_firmware"),
                    path("add-device/", GroupAddDeviceApi.as_view(), name="add_device"),
                    path("add-wifi/", GroupAddWifiApi.as_view(), name="add_wifi"),
                    path("initialize-ota/<uuid:uuid>/", GroupInitializeOtaApi.as_view(), name="initialize_ota"),
                    path("link-api-key/<uuid:group_uuid>/<uuid:api_key_uuid>/", GroupLinkApiKeyApi.as_view(),name="link_api_key"),
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
                    path("<uuid:uuid>/", GroupUpdateApi.as_view(), name="update_group"),
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
                    path("<uuid:uuid>/", GroupDeleteApi.as_view(), name="delete_group"),
                    path("remove-device/<uuid:group_uuid>/<uuid:device_uuid>/",GroupRemoveDeviceApi.as_view(),name="remove_device")
                ],
                "delete",
            )
        ),
    ),
]
