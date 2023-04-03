from django.db import models
from employees.models import Employee

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    deliveries = models.IntegerField(default=0)
    worked_hours = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    deliveries_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    bonus_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    isr_retention = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    grocery_vouchers = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Nómina de {self.employee} para el mes {self.month}"