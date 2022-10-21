from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from core.models import FormData
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = User.objects.create_user(username=username,
                                        password=password)

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('signup')
    else:
        return render(request, 'register.html')


def signup(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        return render(request, 'signup.html')
    return render(request, 'submit.html', context={'user': user})


def portfolio(request):
    formdata = FormData()

    formdata.full_name = request.POST.get('full_name')
    formdata.email = request.POST.get('email')
    formdata.phone_no = request.POST.get('phone')
    # formdata.gender = request.POST.get('gender')
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

    user = FormData.objects.get(email=formdata.email)

    return render(request, 'submit.html', context={'user': user})
