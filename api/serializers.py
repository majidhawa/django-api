from rest_framework import serializers
from student_details.models import Student
from teacher_details.models import Teacher
from classes.models import Class_details
from courses.models import Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class ClassDetailsSerializer(serializers.ModelSerializer):  # Corrected serializer name
    class Meta:
        model = Class_details
        fields = '__all__'