from django.db import models
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    hire_date = models.DateField()
    is_fulltime = models.BooleanField(default=True)
    office_number = models.CharField(max_length=10)
    subjects_taught = models.TextField()









# Create your models here.
