from django.urls import include, path

from rest_framework_simplejwt.views import TokenVerifyView,TokenRefreshView
from apps.authentication.api import (
    UserSessionLoginApi,
    UserSessionLogoutApi, 
    UserJwtLoginApi,
    UserJwtLogoutApi,
    UserMeApi
)


urlpatterns = [
    path(
        "session/",
        include(
            (
                [
                    path("login", UserSessionLoginApi.as_view(), name="login"),
                    path("logout", UserSessionLogoutApi.as_view(), name="logout"),
                ],
                "session",
            )
        ),
    ),
    path(
        "token/",
        include(
            (
                [
                    path("login", UserJwtLoginApi.as_view(), name="login"),
                    path("logout", UserJwtLogoutApi.as_view(), name="logout"),
                    path('verify', TokenVerifyView.as_view(), name='token_verify'),
                    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
                ],
                "token",
            )
        ),
    ),
    path("me", UserMeApi.as_view(), name="me"),
]