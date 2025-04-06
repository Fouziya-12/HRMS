from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class  JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRole
        fields = '__all__'

class  EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'

class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields ='__all__'

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class ProjectAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAssignment
        fields = '__all__'

class EmployeeBenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBenefits
        fields = '__all__'

class EmployeeDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDocuments
        fields = '__all__'

class EmployeeEmergencyContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEmergencyContacts
        fields = '__all__'

class PerformanceGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceGoals
        fields = '__all__'

class EmployeePromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePromotions
        fields = '__all__'

class EmployeeResignationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeResignations
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
        
class ResourceAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ResourceAllocation
        fields = '__all__'


