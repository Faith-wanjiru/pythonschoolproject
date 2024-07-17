from django.urls import path
from .view import StudentListView

urlpatterns = [
    path("Students/", StudentListView.as_view(), name="student_list_view"),
    path("Teachers/", TeachersListViews.as_view(), name="teachers_list_view"),
    path("Courses/", CoursesListViews.as_view(), name="courses_list_view"),
    path("Classperiod/", ClassPeriodListView.as_view(), name="student_list_view"),
    # path("class_period", Class_PeriodListViews.as.view(),="class_period_list_view")

]
   