from django.db import models, connection
from employees.models import Employee

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    deliveries = models.IntegerField(default=0)
    worked_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deliveries_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    bonus_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    isr_retention = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    grocery_vouchers = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # When creating a payroll automatically the stored procedure is called to calculate the payroll
    @classmethod
    def create(cls, employee_id, month, deliveries, worked_hours):
        try:
            with connection.cursor() as cursor:
                # Call the stored procedure passing in the parameters
                cursor.callproc('calculate_payroll', [employee_id, month, deliveries, worked_hours])
            return True
        except:
            return False
        finally:
            # close the transaction
            cursor.close()
    
    def __str__(self):
        return f"Nómina de {self.employee} para el mes {self.month}"