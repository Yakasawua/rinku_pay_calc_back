from django.urls import path
from . import views

urlpatterns = [
    path('list_by_month_year/', views.PayrollListByMonthYear.as_view()), # get payroll list through a post
    path('create/', views.create_payroll), # Create the payroll
]