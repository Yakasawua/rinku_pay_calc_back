from django.urls import path
from . import views

urlpatterns = [
    path('list_by_month_year/', views.PayrollListByMonthYear.as_view()),
    path('create/', views.create_payroll), # Create the payroll
]