from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import DirectCompanyViewSet

router = routers.DefaultRouter()
router.register('direct_company', DirectCompanyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]