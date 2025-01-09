from django.urls import include, path

from apps.role.api import (
    RolesListApi,
)


urlpatterns = [
    path(
        "get/",
        include(
            (
                [
                    path("list/all", RolesListApi.as_view(), name="list_role"),
                ],
                "get",
            )
        ),
    ),
]