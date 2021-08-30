from django.shortcuts import render, redirect
from .models import IndiviualRequest, CompanyRequest
from .models import User
from django.contrib.auth import authenticate, logout, login


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('home-page')
    return render(request, 'main/home.html')


def all_individual(request):
    all = IndiviualRequest.objects.all()
    return render(request, 'main/all_individual.html', context={"all": all})


def use_dash(request):
    context = {"user": User.objects.get(pk=request.user.pk)}
    return render(request, 'main/user-dash.html', context=context)


def add_individual_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        user = User.objects.create_empuser(email=email, first_name=first_name, last_name=last_name, password=password,
                                           address=country, phone=phone)
        individual = IndiviualRequest(first_name=first_name, last_name=last_name, phone=phone, country=country, DOB=dob,
                                      email=email)
        individual.save()
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    else:
        return render(request, 'main/indiviual.html', )


def logoutUser(request):
    logout(request)
    return redirect('home-page')


def add_company_request(request):
    if request.method == 'POST':
        company_email = request.POST.get('email')
        company_name = request.POST.get('company_name')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        dob = request.POST.get('dob')
        company = CompanyRequest(area_created=country, main_phone=phone, main_email=company_email,
                                 company_name=company_name, DOC=dob)
        company.save()
        return redirect('home-page')
    else:
        return render(request, 'main/company.html', )
