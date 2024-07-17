from django.urls import path
from views import StudentListView


urlpatterns=[
    path("student/, StudentListView.as_view(), name=student_list_view"),
    path("course/, CourseListView.as_view(), name=course_list_view"),
    path("teacher/, TeacherListView.as_view(), name=teacher_list_view"),
    path("class_period/ClassPeriodListView.as_view(), name=class_period_list_view"),
    path("rest_framework/RestframeworkListView.as_view(), name=rest_framework_list_view"),
]

https://127.0.0/:8000/api/students/