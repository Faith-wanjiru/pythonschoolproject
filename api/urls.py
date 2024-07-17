from django.urls import path
from .view import StudentListView
from .view import TeacherListView
from .view import CoursesListView
from .views import ClassPeriod

urlpatterns = [
    path("Students/", StudentListView.as_view(), name="student_list_view"),
    path("Teacher/", TeacherListViews.as_view(), name="teacher_list_view"),
    path("Courses/", CoursesListViews.as_view(), name="courses_list_view"),
    path("Classperiod/", ClassPeriodListView.as_view(), name="classperiod_list_view"),
    # path("class_period", Class_PeriodListViews.as.view(),="class_period_list_view")

]
   