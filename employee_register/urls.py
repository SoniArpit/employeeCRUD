from django.contrib import admin
from django.urls import path, include
from employee_register import views

urlpatterns = [
    path('', views.employee_form, name="employee_insert"),
    path('<int:id>/', views.employee_form,
         name="employe_update"),  # for update link
    path('delete/<int:id>/', views.employee_delete, name="employee_delete"),
    path('list/', views.employee_list, name="employee_list"),
]
