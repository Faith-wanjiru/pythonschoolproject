from rest_framework.response import Response
from rest_framework.views import Student
from student.models import Student
from .serializers import StudentSerializer

class StudentListView(APIView):
    def get(self,request):
        students=Students.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data)

