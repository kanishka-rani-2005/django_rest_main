from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse

from students.models import Student
from api.serializers import StudentSerializer,EmployeesSerializer,BlogSerializer,CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from employees.models import Employees
from blogs.models import Blog,Comment
from rest_framework.views import APIView
from django.http import Http404

from .pagination import CustomPagination 
from rest_framework.filters import SearchFilter,OrderingFilter

# MANUAL WAY TO SERIALIZE 
# Create your views here.
# def studentsView(request):
#     students=Student.objects.all()
#     students_list=list(students.values()) #manual way to serialize
       
#     return JsonResponse(students_list,safe=False)


@api_view(['GET','POST'])
def studentsView(request):
    if request.method=='GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.error_messages)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def studentsDetailsView(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

# class EmployeesView(APIView):
#     def get(self,request):
#         employees=Employees.objects.all()
#         serializer=EmployeesSerializer(employees,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer=EmployeesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    


# class EmployeesDetailsView(APIView):
#     def get_object(self,pk):
#         try:
#             return Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist:
#             raise Http404
        
#     def get(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmployeesSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
        

#     def put(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmployeesSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         employee=self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    




# MIXINS <- Easy than generic way
# from rest_framework import mixins,generics

# class EmployeesView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Employees.objects.all()
#     serializer_class=EmployeesSerializer

#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)

 
# class EmployeesDetailsView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Employees.objects.all()
#     serializer_class=EmployeesSerializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk)
    
#     def post(self,request,pk):
#         return self.update(request,pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
    

    


# GENERICS <-EASIER THAN MIXINS

# from rest_framework import generics

# class EmployeesView(generics.ListAPIView,generics.CreateAPIView):
#     queryset=Employees.objects.all()
#     serializer_class=EmployeesSerializer


# class EmployeesDetailsView(generics.RetrieveAPIView,generics.DestroyAPIView,generics.UpdateAPIView):
#     queryset=Employees.objects.all()
#     serializer_class=EmployeesSerializer
#     lookup_field='pk'


# class EmployeesView(generics.ListCreateAPIView):
#     queryset=Employees.objects.all()
#     serializer_class=EmployeesSerializer


# class EmployeesDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Employees.objects.all()
#     serializer_class=EmployeesSerializer
#     lookup_field='pk'
    




# VIEWSETS 
# from rest_framework import viewsets

# class EmployeesViewset(viewsets.ViewSet):
#     def list(self,request):
#         queryset=Employees.objects.all()
#         serializer=EmployeesSerializer(queryset,many=True)
#         return Response(serializer.data)
#     def create(self,request):
#         serializer=EmployeesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self,request,pk=None):
#         employee=get_object_or_404(Employees,pk=pk)
#         serializer=EmployeesSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def update(self,request,pk=None):
#         employee=get_object_or_404(Employees,pk=pk)
#         serializer=EmployeesSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def delete(self,request,pk=None):
#         employee=get_object_or_404(Employees,pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import viewsets
from .filters import EmployeeFilter
# Both <- primary key operations and non-primary keynoperations
class EmployeesViewset(viewsets.ModelViewSet):
    queryset=Employees.objects.all()
    serializer_class=EmployeesSerializer
    pagination_class=CustomPagination
    filterset_class=EmployeeFilter

from rest_framework import generics
class BlogsView(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['^blog_title','blog_body'] # ^ starts with that keyword
    ordering_fields=['id','blog_title']


class CommentsView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer


class BlogsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field='pk'

class CommentsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    lookup_field='pk'


 