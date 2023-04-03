from rest_framework import serializers
from .models import Payroll
from employees.serializers import EmployeeNameNumberSerializer

class PayrollSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payroll
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeNameNumberSerializer(instance['employee']).data
        return response