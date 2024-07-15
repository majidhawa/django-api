from django.urls import path
from .views import StudentListView, TeacherListView, CourseListView, ClassesListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list_view'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list_view'),
    path('courses/', CourseListView.as_view(), name='course_list_view'),  # Fixed typo in name attribute
    path('classes/', ClassesListView.as_view(), name='classes_list_view'),  # Added missing slash and fixed typo
]
