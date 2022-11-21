from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Users

# Create your views here.


def employee_list(request):
    context = {'employee_list': Users.objects.all()}
    return render(request, "register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            user = Users.objects.get(pk=id)
            form = EmployeeForm(instance=user)
        return render(request, "register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            user = Users.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= user)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    user = Users.objects.get(pk=id)
    user.delete()
    return redirect('/employee/list')
