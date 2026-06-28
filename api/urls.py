from django.urls import path, include
from . import views
urlpatterns = [
    path('student/', views.studentViews),
    path("student/<int:pk>/", views.studentDetailViews)

]