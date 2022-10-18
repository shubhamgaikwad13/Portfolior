from django.shortcuts import render
from core.models import FormData
# Create your views here.


def index(request):
    return render(request, 'index.html')


def portfolio(request):
    formdata = FormData()

    formdata.full_name = request.POST.get('full_name')
    formdata.email = request.POST.get('email')
    formdata.phone_no = request.POST.get('phone')
    formdata.gender = request.POST.get('gender')
    formdata.date_of_birth = request.POST.get('dob')

    formdata.highest_edu = request.POST.get('education')
    formdata.specialization = request.POST.get('edu_major')
    formdata.institute_name = request.POST.get('institute')
    formdata.year_of_completion = request.POST.get('completion_year')

    formdata.current_organization = request.POST.get('org')
    formdata.current_role = request.POST.get('role')
    formdata.date_of_joining = request.POST.get('joining_date')
    formdata.emp_type = request.POST.get('emp_type')

    formdata.save()

    user = FormData.objects.get(email="sm@mail.com")

    return render(request, 'pf.html', context={'user': user})
