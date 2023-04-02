from django.db import models, connection

class Employee(models.Model):
    EMPLOYEE_ROLES = (
        ('CH', 'Chofer'),
        ('CA', 'Cargador'),
        ('AU', 'Auxiliar'),
    )
    
    employee_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=2, choices=EMPLOYEE_ROLES)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, default=30.00)
    deliveries_payment = models.DecimalField(max_digits=10, decimal_places=2, default=5.00)
    bonus_hourly = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @classmethod
    def create(cls, emp_num, emp_name, emp_role):
        try:
            with connection.cursor() as cursor:
                # Call the stored procedure passing in the parameters
                cursor.callproc('create_employee', [emp_num, emp_name, emp_role])
            return True
        except:
            return False
        finally:
            # close the transaction
            cursor.close()
            
    # def save(self, *args, **kwargs):
    #     if self.role == 'CH':
    #         self.bonus_hourly = 10
    #     elif self.role == 'CA':
    #         self.bonus_hourly = 5
    #     super(Employee, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name