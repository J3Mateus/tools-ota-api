from django.urls import include, path

urlpatterns = [
    path("wifi/", include(("apps.wifi.urls", "Wifi"))),
    path("group/", include(("apps.group.urls", "Group"))),
    path("device/", include(("apps.device.urls", "Device"))),
    path("firmware/", include(("apps.firmware.urls", "Firmware"))),
        # path("firmware/", include(("apps.firmware.urls", "Firmware"))),
]
