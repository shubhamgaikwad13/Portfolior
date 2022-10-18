from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class FormData(models.Model):
    # personal info
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    gender = models.CharField(max_length=6)
    date_of_birth = models.DateField()

    # education info
    highest_edu = models.CharField(max_length=20)
    specialization = models.CharField(max_length=50)
    institute_name = models.CharField(max_length=100)
    year_of_completion = models.CharField(max_length=4)

    # professional info
    current_organization = models.CharField(max_length=100)
    current_role = models.CharField(max_length=50)
    date_of_joining = models.CharField(max_length=20)
    emp_type = models.CharField(max_length=20)
