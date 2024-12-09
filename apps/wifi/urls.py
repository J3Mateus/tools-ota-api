from django.urls import include, path

from apps.wifi.api import (
    WifiCreateApi,
    WifiListApi,
    WifiUpdateApi,
    WifiDeleteApi,
    WifiByIDApi
)

urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("", WifiListApi.as_view(), name="list_wifi"),
                    path("<uuid:uuid>", WifiByIDApi.as_view(), name="wifi_by_id"),
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
                    path("", WifiCreateApi.as_view(), name="create_wifi"),
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
                    path("<uuid:uuid>", WifiUpdateApi.as_view(), name="update_wifi"),
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
                    path("<uuid:uuid>", WifiDeleteApi.as_view(), name="delete_wifi"),
                ],
                "delete",
            )
        ),
    ),
]
