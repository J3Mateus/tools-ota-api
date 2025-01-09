from django.urls import include, path
from apps.users.api import (
    UserCreateApiKeyApi,
    UserCreateApi,
    UserListApiKeyApi,
    KeyByIDApi,
    KeyUpdateApi,
    KeyDeleteApi
)


urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("api-key/list",UserListApiKeyApi.as_view(),name="list_api_Key"),
                    path("api-key/<uuid:uuid>", KeyByIDApi.as_view(), name="key_by_id"),
                ],
                "list"
            )
        )
    ),
    path(
        "create/",
        include(
            (
                [
                    path("api-key", UserCreateApiKeyApi.as_view(), name="create_api_key"),
                    path("", UserCreateApi.as_view(), name="create"),
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
                    path("api-key/<uuid:uuid>", KeyUpdateApi.as_view(), name="update_key"),
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
                    path("api-key/<uuid:uuid>", KeyDeleteApi.as_view(), name="delete_key")
                ],
                "delete",
            )
        ),
    ),
]
