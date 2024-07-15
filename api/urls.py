from django.urls import path
from .view import StudentListView

urlpatterns = [
    path("Students/", StudentListView.as_view(), name="student_list_view"),
    path("Teachers/", TeacherListViews.as_view(), name="teacher_list_view"),
    path("Courses/", CourseListViews.as_view(), name="course_list_view"),
    path("Class_period/", ClassroomListView.as_view(), name="student_list_view"),
    path("class_period", Class_PeriodListViews.as.view(),="class_period_list_view")

]
   