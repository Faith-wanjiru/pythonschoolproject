from django.db import models

# from django.db import Classroom
# from classroom.models import Classroom
# from course.models import Course


class Class_Period(models.Model):
      class_id=models.AutoField(primary_key=True)
      class_name=models.CharField(max_length=30)
      class _start_time = models.TimeField()
        class _end_date= models.TimeField()
        class _Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='student_class')
        class _Classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='course')
        class _dayofweek = models.CharField(max_length=30)
        class _created_at=models.DateField()
        class _updated_at=models.DateField()
     def __str__(self):
        return self.name

# Create your models here.


