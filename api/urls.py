from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassPeriodListView

urlpatterns = [
    path("Students/", StudentListView.as_view(), name="student_list_view"),
    path("Teacher/", TeacherListView.as_view(), name="teacher_list_view"),
    path("Courses/", CourseListView.as_view(), name="course_list_view"),
    path("Classperiod/", ClassPeriodListView.as_view(), name="classperiod_list_view"),
    # path("class_period", Class_PeriodListViews.as.view(),="class_period_list_view")
    path ("students/<int:id>/",StudentDetailView.as_view(), name="student_detail_view")
    
    path ("teacher/<int:id>/",TeacherDetailView.as_view(), name="teacher_detail_view")

    path ("classperiod/<int:id>/",ClassPeriodDetailView.as_view(), name="classperiod_detail_view")

    path ("course/<int:id>/",CourseDetailView.as_view(), name="student_detail_view")

    path ("classroom/<int:id>/",ClassRoomDetailView.as_view(), name="student_detail_view")


    

]
   