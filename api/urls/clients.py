from rest_framework.routers import DefaultRouter

import api.views.clients as views

router = DefaultRouter()
router.register("clients", views.ClientAPIView)

urlpatterns = router.urls
