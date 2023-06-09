# Generated by Django 4.0.4 on 2023-04-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('CH', 'Chofer'), ('CA', 'Cargador'), ('AU', 'Auxiliar')], max_length=2)),
                ('base_salary', models.DecimalField(decimal_places=2, default=30.0, max_digits=10)),
                ('deliveries_payment', models.DecimalField(decimal_places=2, default=5.0, max_digits=10)),
                ('bonus_hourly', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
