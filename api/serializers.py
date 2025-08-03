from rest_framework import serializers
from students.models import Student
from employees.models import Employees
from blogs.models import Blog,Comment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields='__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'      

class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Blog
        fields='__all__' 

        



