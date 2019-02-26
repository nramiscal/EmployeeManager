from django.shortcuts import render
from .models import *

# User.objects.create(fname='Manny', lname='Ramiscal', manager_id=1)

def index(request):
    users = User.objects.all()
    return render(request, "myapp/index.html", {'users':users})

def manager(request, manager_id):
    manager = User.objects.get(id=manager_id)
    employees = manager.employees.all()
    context = {
        'manager' : manager,
        'employees' : employees
    }

    return render(request, "myapp/manager.html", context)
