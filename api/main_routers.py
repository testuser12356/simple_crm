from django.urls import path, include

urlpatterns = [
    path("", include("api.urls.tasks")),
    path("", include("api.urls.clients")),
    path("user/", include("api.urls.custom_user"))
]
