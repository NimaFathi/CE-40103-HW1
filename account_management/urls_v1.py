from django.conf.urls import url, include

from rest_framework import routers

from account_management.views import AccountViewSet
from account_management.views import LogInView

router = routers.DefaultRouter()
router.register('acc', AccountViewSet, basename='account')

urlpatterns = [
                  url(r'login/', view=LogInView.as_view(), name='login'),

] + router.urls
