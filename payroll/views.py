from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import Payroll

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