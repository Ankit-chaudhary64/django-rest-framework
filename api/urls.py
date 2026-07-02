from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register('employee', views.EmployeesViewSet, basename= 'employee')
urlpatterns = [
    path('student/', views.studentViews),
    path("student/<int:pk>/", views.studentDetailViews),
    path('',include(router.urls)),

    
    # path('employee/', views.Employees.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetail.as_view()),

]