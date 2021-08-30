from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('create/individual', views.add_individual_request, name='add-individual'),
    path('create/company', views.add_company_request, name='add-company'),
    path('dashboard', views.use_dash, name='dashboard'),
    path('logout', views.logoutUser, name='logout'),
    path('all/individual', views.all_individual, name='all'),
    path('about', views.about_page, name='about'),
    path('ethics', views.ethics, name='ethics'),

]