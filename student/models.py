from django.db import models
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    code=models.PositiveSmallIntegerField(max_length=4)
    date_of_birth=models.DateField()
    country=models.CharField(max_length=20)
    bio=models.TextField()
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
                       


