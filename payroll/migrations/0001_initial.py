# Generated by Django 4.0.4 on 2023-04-03 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField()),
                ('deliveries', models.IntegerField(default=0)),
                ('worked_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('deliveries_payment', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('bonus_payment', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('isr_retention', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('grocery_vouchers', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]
