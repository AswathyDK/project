from django.urls import path
from . import views

urlpatterns = [
    path('advocatehome/', views.advocatehome, name='advocatehome'),  # advocateHome
    # updateadvocateprofile
    path('advocateprofile/', views.advocateprofile, name='advocateprofile'),
    # viewadvocateprofile
    path('viewadvocateprofile/', views.viewadvocateprofile, name='viewadvocateprofile'),
    path('viewcasedetails/', views.viewcasedetails, name='viewcasedetails'),
    path('confirmedcases/', views.confirmedcases, name='confirmedcases'),
    path('addsitting/<int:casedetailsid>/', views.addsitting, name='addsitting'),
    path('sittings/', views.sittings, name='sittings'),
    path('confirmpayment/<int:sittingid>/', views.confirmpayment, name='confirmpayment'),
    path('viewcasedetails2/', views.viewcasedetails2, name='viewcasedetails2'),
    path('updatecasestatus/', views.updatecasestatus, name='updatecasestatus'),
    # path('updatecasestatus/', views.updatecasestatus, name='updatecasestatus'),

]
