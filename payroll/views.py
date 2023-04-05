from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import JsonResponse
from django.db import connection


from .models import Payroll
from .serializers import PayrollSerializer
from employees.models import Employee

@api_view(['POST'])
def create_payroll(request):
    # Get the employee_number, name and role parameters
    employee_id = request.data['employee_id']
    month = request.data['month']
    deliveries = request.data['deliveries']
    worked_hours = request.data['worked_hours']
    # Create the payroll
    playroll = Payroll.create(employee_id, month, deliveries, worked_hours)

    if playroll:
        return JsonResponse({'status': 'OK', 'message': 'Playroll created successfully.'},status=status.HTTP_200_OK)
    return JsonResponse({'status': 'Error', 'message': 'Error creating playroll.'}, status=status.HTTP_400_BAD_REQUEST)

def tuple_to_dict(payroll_data):
    payroll_list = []
    for payroll in payroll_data:
        # You can't just send an id, you have to send the Employee object
        exployee = Employee.objects.get(id=payroll[9])
        payroll_dict = {
            'id': payroll[0],
            'month': payroll[1],
            'deliveries': payroll[2],
            'worked_hours': payroll[3],
            'deliveries_payment': payroll[4],
            'bonus_payment': payroll[5],
            'isr_retention': payroll[6],
            'grocery_vouchers': payroll[7],
            'total_salary': payroll[8],
            'employee': exployee
        }
        payroll_list.append(payroll_dict)
    return payroll_list

class PayrollListByMonthYear(APIView):
    def post(self, request, format=None):
        month_year = request.data['month_year']
        cursor = connection.cursor()
        # Call the stored procedure passing in the parameter
        cursor.callproc('payroll_list_by_month_year', [month_year])
        # The database returns a tuple
        results = cursor.fetchall()
        cursor.close()
        # We convert that tuple into a dict
        payroll_list = tuple_to_dict(results)
        # We use a serializer to transform it into a json
        serializer = PayrollSerializer(payroll_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)