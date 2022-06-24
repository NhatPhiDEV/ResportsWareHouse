from django.urls import path,include
from rest_framework import routers
from reports.views import DepartmentsViewSet, ReportsViewSet
router = routers.DefaultRouter()
router.register('reports',ReportsViewSet, 'reports')
router.register('departments',DepartmentsViewSet, 'departments')
urlpatterns = [
    path('',include(router.urls))
]