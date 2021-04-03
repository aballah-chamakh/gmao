from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import AffiliateCompanyViewSet

router = routers.DefaultRouter()
router.register('affiliate_company', AffiliateCompanyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]