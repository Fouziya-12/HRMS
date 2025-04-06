from rest_framework import viewsets
from .models import Employee,Department,JobRole
from .serializers import DepartmentSerializer,EmployeeSerializer,JobRoleSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class JobRoleViewSet(viewsets.ModelViewSet):
    queryset = JobRole.objects.all()
    serializer_class = JobRoleSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .models import Department           # already import 
# from .serializers import DepartmentSerializer

@api_view(["POST"])
def create_department(request): 
    # De-serialize the incoming data
    serializer = DepartmentSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
