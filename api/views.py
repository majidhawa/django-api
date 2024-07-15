from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from teacher_details.models import Teacher
from courses.models import Course
from classes.models import Class_details
from student_details.models import Student
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import CourseSerializer
from .serializers import ClassDetailsSerializer  

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

class CourseListView(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class ClassDetailsListView(APIView):  
    def get(self, request, format=None):
        classes = Class_details.objects.all()
        serializer = ClassDetailsSerializer(classes, many=True)  
        return Response(serializer.data)
