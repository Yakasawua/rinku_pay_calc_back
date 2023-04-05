from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from django.http import JsonResponse

from .models import Employee
from .serializers import EmployeeSerializer

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

# The database returns a tuple, so it has to be transformed to a dictionary for the serializer
def tuple_to_dict(employees_data):
    employee_list = []
    for employee in employees_data:
        employee_dict = {
            'id': employee[0],
            'employee_number': employee[1],
            'name': employee[2],
            'role': employee[3],
            'base_salary': employee[4],
            'deliveries_payment_employee': employee[5],
            'bonus_hourly': employee[6]
        }
        employee_list.append(employee_dict)
    return employee_list

class EmployeeListView(APIView):
    def get(self, request, format=None):
        cursor = connection.cursor()
        # Call the stored procedure
        cursor.callproc('get_all_employees')
        # The database returns a tuple
        results = cursor.fetchall()
        cursor.close()
        # We convert that tuple into a dict
        employee_list = tuple_to_dict(results)
        # We use a serializer to transform it into a json
        serializer = EmployeeSerializer(employee_list, many=True)
        return Response(serializer.data)