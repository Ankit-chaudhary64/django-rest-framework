from django.urls import path, include
from . import views
urlpatterns = [
    path('student/', views.studentViews),
    path("student/<int:pk>/", views.studentDetailViews),

    
    path('employee/', views.Employees.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),

]