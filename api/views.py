from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classperiod.models import ClassPeriod
from classroom.models import ClassRoom
from .serializers import StudentSerializer
from .serializers import CourseSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer
from .serializers import ClassRoomSerializer


class StudentListView(APIView):
    def get(self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student, many=True)
        return Response(serializer.data)

#Post Method 
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= Student.HTTP_400_BAD_REQUEST)
        
# Detail View
class StudentDetailView(APIView):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    
# Put Method
class StudentDetailView(APIView):
    def put(self, request, id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student, data=requestdata)
        if serializer is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_20_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# Delete Method
    def delete(self,request,id):
        student=Student.objects.get(id=id):
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)



class CourseListView(APIView):
    def get(self,request):
        course=Course.objects.all()
        serializer=CourseSerializer(course, many=True)
        return Response(serializer.data)
    
# Post Method 
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= Course.HTTP_400_BAD_REUEST)
    

# DetailView
class CourseDetailView(APIView):
    def get(self,request,id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    


# Put Method
class CourseDetailView(APIView):
    def put(self, request, id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course, data=requestdata)
        if serializer is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_20_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# Delete Method

    def delete(self,request,id):
        course=Course.objects.get(id=id):
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

class TeacherListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all()
        serializer=TeacherSerializer(teacher, many=True)
        return Response(serializer.data)


# Post Method 
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= Teacher.HTTP_400_BAD_REQUEST)


# DetailView
class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher)
        return Response(serializer.data)
    

# Put Method
class TeacherDetailView(APIView):
    def put(self, request, id):
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher, data=requestdata)
        if serializer is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_20_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# Delete Method

    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id):
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ClassPeriodListView(APIView):
    def get(self,request):
        classperiod=ClassPeriod.objects.all()
        serializer=ClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)
    

# Post Method 
    def post(self,request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= ClassPeriod.HTTP_400_BAD_REUEST)
        

# DetailView
class ClassPeriodDetailView(APIView):
    def get(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(ClassPeriod)
        return Response(serializer.data)
    

# Put Method
class ClassDetailView(APIView):
    def put(self, request, id):
        classperiod=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod, data=requestdata)
        if serializer is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_20_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Delete Method

    def delete(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id):
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    
class ClassRoomListView(APIView):
    def get(self,request):
        classroom=ClassRoom.objects.all()
        serializer=ClassRoomSerializer(classroom, many=True)
        return Response(serializer.data)


   # Post Method 
    def post(self,request):
        serializer = ClassRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= ClassRoom.HTTP_400_BAD_REUEST) 
        


# DetailView
class ClassRoomDetailView(APIView):
    def get(self,request,id):
        classroom=ClassRoom.objects.get(id=id)
        serializer=ClassRoomSerializer(ClassPeriod)
        return Response(serializer.data)



# Put Method
class ClassRoomView(APIView):
    def put(self, request, id):
        ClassRoom=ClassRoom.objects.get(id=id)
        serializer=ClassRoomSerializer(ClassRoom, data=requestdata)
        if serializer is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_20_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



        # Delete Method

    def delete(self,request,id):
        classperiod=ClassRoom.objects.get(id=id):
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)