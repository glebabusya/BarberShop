from rest_framework import routers
from employers import views

router = routers.SimpleRouter()
router.register(r"employers", views.EmployeeViewSet)

urlpatterns = []
urlpatterns += router.urls
