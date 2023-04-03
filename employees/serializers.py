from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeNameNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'employee_number',)