from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import Employee

@api_view(['POST'])
def create_employee(request):
    # Get the employee_number, name and role parameters
    employee_number = request.data['employee_number']
    name = request.data['name']
    role = request.data['role']
    # Create the employee
    employee = Employee.create(employee_number, name, role)

    if employee:
        return JsonResponse({'status': 'OK', 'message': 'Employee created successfully.'},status=status.HTTP_200_OK)
    return JsonResponse({'status': 'Error', 'message': 'Error creating employee.'}, status=status.HTTP_400_BAD_REQUEST)