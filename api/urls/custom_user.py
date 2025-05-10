from django.urls import path
from rest_framework.routers import DefaultRouter

import api.views.custom_user as views

router = DefaultRouter()
router.register("create", views.CreateCustomUserView)

urlpatterns = [
                  path("get-me", views.GetMe.as_view())
              ] + router.urls
