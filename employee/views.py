from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from .models import Employee


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        gender = postData.get('gender')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        print(first_name, last_name, gender, phone, email, password)
        employee = Employee(first_name=first_name,
                            last_name=last_name,
                            gender=gender,
                            phone=phone,
                            email=email,
                            password=password)
        employee.register()
        return render(request, 'login.html')

def login(request):
    if request.method == 'GET':
        return render(request, "login.html", )
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        employee = Employee.get_employee_by_email(email)
        error_message = None
        if employee:
            flage = check_password(password, employee.password)
            if flage:
                return redirect("employee.html")
            else:
                error_message = "Email or password invalid"
        else:
            error_message = "Email or password invalid"
        print(employee)
        print(email, password)
        return render(request, "employee.html", {'error': error_message})

def employee(request):
    employee = Employee.objects.all()
    d = {'employee': employee}
    return render(request, 'employee.html', d)

