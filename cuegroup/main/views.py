from django.shortcuts import render, redirect
from .models import IndiviualRequest, CompanyRequest


# Create your views here.
def home_page(request):
    return render(request, 'main/home.html')


def add_individual_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        dob = request.POST.get('dob')
        individual = IndiviualRequest(first_name=first_name, last_name=last_name, phone=phone, country=country, DOB=dob,
                                      email=email)
        individual.save()
        return redirect('home-page')
    else:
        return render(request, 'main/indiviual.html', )



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
