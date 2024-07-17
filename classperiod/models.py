from django.db import models

# from django.db import Classroom
# from classroom.models import Classroom
# from course.models import Course


class ClassPeriod(models.Model):
      class_id=models.AutoField(primary_key=True)
      class_name=models.CharField(max_length=30)
      class_start_time = models.TimeField()
      class_end_date= models.TimeField()
      # class_course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True, related_name = "student_class")
      # class_classroom = models.ForeignKey("classroom", on_delete=models.SET_NULL, null=True, related_name = "course")
      class_dayofweek = models.CharField(max_length=30)
      # class_created_at=models.DateField()
      # class_updated_at=models.DateField()
def __str__(self):
        return self.name

# Create your models here.


