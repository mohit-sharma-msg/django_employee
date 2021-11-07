from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500, null=True)

    def register(self):
        self.save()

    def _str_(self):
        return self.user.username

    @staticmethod
    def get_employee_by_email(email):
        return Employee.objects.get(email=email)
