from django.db import models

#1. Department Table
class Department(models.Model):
    dno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=100,unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.dname

#2. JobRole
class JobRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100,unique=True)
    description = models.TextField()

    def __str__(self):
        return self.role_name

#3. Employee 
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    position = models.ForeignKey(JobRole,on_delete=models.SET_NULL,null=True,blank=True)  # Reference to JobRole
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)  # Optional department
    hire_date = models.DateField()  
    salary = models.DecimalField(max_digits=10,decimal_places=2)  # Promised salary
    manager = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,related_name='subordinates') # self-referential FK for hierarchy

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#4. Attendance  
class Attendance(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.employee}-{self.date}-{self.status}"

#5. Salaries  
class Salaries(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.employee}-{self.date}-{self.amount}"

#6. Leaves   
class Leave(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)  
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=20) # ex - sick leave,urgent leave etc
    status = models.CharField(max_length=10) # ex - approved,pending,rejected

    def __str__(self):
        return f"{self.employee}-{self.leave_type}-{self.start_date}to{self.end_date}"
    
#7. Performance review table
class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    review_date = models.DateField()
    rating = models.IntegerField()  # ex - 1 to 5
    feedback = models.TextField()

    def __str__(self):
        return f"{self.employee} - {self.review_date} - Rating: {self.rating}"
    
#8. Training Table
class Training(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    training_date = models.DateField()
    topic = models.CharField(max_length=100)
    duration = models.DecimalField(max_digits=5,decimal_places=2)  # duartion hours

    def __str__(self):
        return f"{self.employee} - {self.topic} - {self.training_date}"

#9. Project Assignment
class ProjectAssignment(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.project_name} - {self.role}"

#10. Employee Benefits
class EmployeeBenefits(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    benefit_type = models.CharField(max_length=50) # ex - health insurance,retirment plan
    provider = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"{self.employee} - {self.benefit_type}"
    
#11. Employee Documents
class EmployeeDocuments(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    dcument_type = models.CharField(max_length=50) # ex - contract,certificates
    upload_date = models.DateField()
    documents = models.FileField(upload_to='documents/')
    description = models.TextField(null=True,blank=True)

    def __str__(self):
       return f"{self.employee} - {self.document_type}"
    
#12. EMPLOYEE EMERGENCY CONTACTS TABLE 
class EmployeeEmergencyContacts(models.Model): 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)

    def _str_(self):
        return f"{self.employee} - {self.name} - {self.relationship}"
    
#13. PERFORMANCEGOALS TABLE
class PerformanceGoals(models.Model):  
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    goal_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)  # E.g., In Progress, Completed

    def _str_(self):
        return f"{self.employee} - {self.goal_description} - {self.status}"
    
#14. EMPLOYEEPROMOTIONS TABLE
class EmployeePromotions(models.Model): 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    old_position = models.CharField(max_length=50)
    new_position = models.CharField(max_length=50)
    promotion_date = models.DateField()

    def _str_(self):
        return f"{self.employee} - {self.old_position} to {self.new_position}"
    
#15. EMPLOYEERESIGNATIONS TABLE
class EmployeeResignations(models.Model): 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    resignation_date = models.DateField()
    reason = models.TextField()

    def _str_(self):
        return f"{self.employee} - {self.resignation_date}"
    
#16. RESOURCES TABLE
from django.db import models
class Resource(models.Model):  
    resource_name = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50)  # E.g., Laptop, Phone, etc.
    resource_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20)  # E.g., Available, Assigned, etc.

    def _str_(self):
        return f"{self.resource_name} ({self.resource_type}) - {self.resource_id}"
    
     
#17. RESOURCEALLOCATION TABLE
class ResourceAllocation(models.Model): 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    allocation_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)  # E.g., Assigned, Returned, etc.

    def _str_(self):
        return f"{self.resource} assigned to {self.employee} on {self.allocation_date}"





        
    

    
    


    
    
