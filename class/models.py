from django.db import models
class Class(models.Model):
    class_name = models.CharField(max_length=50)
    class_code = models.CharField(max_length=10, unique=True)
    teacher_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    schedule = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    max_students = models.PositiveIntegerField()
    current_students = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

# Create your models here.
