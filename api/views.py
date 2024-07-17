from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer


class StudentListView(APIView):
    def get(self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student, many=True)
        return Response(serializer.data)


class CourseListView(APIView):
    def get(self,request):
        course=Courses.objects.all()
        serializer=CourseSerializer(course, many=True)
        return Response(serializer.data)
    

class TeacherListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all()
        serializer=StudentSerializer(teacher, many=True)
        return Response(serializer.data)



class ClassPeriodListView(APIView):
    def get(self,request):
        classperiod=ClassPeriodListView.objects.all()
        serializer=ClassPeriodSerializer(Class_Period, many=True)
        return Response(serializer.data)

# class StudentListView(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

# class CourseListView(APIView):
#     def get(self, request):
#         courses = Course.objects.all()  # Changed from Courses to Course
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)

# class TeacherListView(APIView):
#     def get(self, request):
#         teachers = Teacher.objects.all()
#         serializer = TeacherSerializer(teachers, many=True)  # Changed to TeacherSerializer
#         return Response(serializer.data)

# class ClassPeriodListView(APIView):
#     def get(self, request):
#         class_periods = ClassPeriod.objects.all()  # Changed to ClassPeriod.objects.all()
#         serializer = ClassPeriodSerializer(class_periods, many=True)
#         return Response(serializer.data)


