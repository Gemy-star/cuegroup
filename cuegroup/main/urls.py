from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('create/individual', views.add_individual_request, name='add-individual'),
    path('create/company', views.add_company_request, name='add-company'),

]