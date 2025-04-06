from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, JobRoleViewSet
from .views import  create_department

router = DefaultRouter()
router.register(r'employees',EmployeeViewSet)
router.register(r'departments',DepartmentViewSet)
router.register(r'jobrole',JobRoleViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/depart/create', create_department,name=' create_department')
]

