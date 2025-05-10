from rest_framework.routers import DefaultRouter

import api.views.tasks as views

router = DefaultRouter()
router.register("tasks", views.TaskAPIView)

urlpatterns = router.urls
