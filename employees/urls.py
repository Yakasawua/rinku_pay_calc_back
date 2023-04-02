from django.urls import path
from . import views

urlpatterns = [
    path('list/',  views.EmployeeListView.as_view()), # List employees
    path('create/', views.create_employee), # Create the employee
]