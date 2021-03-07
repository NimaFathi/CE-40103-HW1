from django.conf.urls import url, include

from rest_framework import routers

from account_management.views import AccountViewSet

router = routers.DefaultRouter()
router.register('acc', AccountViewSet, basename='account')

urlpatterns = [
] + router.urls
