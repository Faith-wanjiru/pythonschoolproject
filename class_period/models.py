from django.db import models

# Create your models here.

from django.db import Classroom
from classroom.models import Classroom
from course.models import Course


class Class_Period(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    start_time=models.TimeField()
    end_date=models.TimeField()
    Course=models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='student_class')
    Classroom=models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='course')
    day_of_week=models.CharField(max_length=30)
    created_at=models.DateField()
    updated_at=models.DateField()
    def __str__(self):
        return self.name
