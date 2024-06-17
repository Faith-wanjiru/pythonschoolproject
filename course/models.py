from django.db import models
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    department = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)
    is_elective = models.BooleanField(default=False)
    prerequisites = models.TextField()
    max_capacity = models.PositiveIntegerField()
    duration_weeks = models.PositiveIntegerField()

# Create your models here.
