from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register('employees',views.EmployeesViewset,basename='employees')



urlpatterns = [
    path("students/",views.studentsView),
    path('students/<int:pk>/',views.studentsDetailsView),
    # path("employees/",views.EmployeesView.as_view()),
    # path('employees/<int:pk>/',views.EmployeesDetailsView.as_view()),
    path('',include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('blogs/<int:pk>/',views.BlogsDetailsView.as_view()),

    path('comments/',views.CommentsView.as_view()),
    path('comments/<int:pk>/',views.CommentsDetailsView.as_view()),
]
