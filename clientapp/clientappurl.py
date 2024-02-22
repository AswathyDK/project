from  django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
#Client Home Page
    path('clienthome/', views.clienthome,name='clienthome'),

#VIEW Advocate details by searching casetypes
    path('casetypeadvocates/', views.casetypeadvocates, name='casetypeadvocates'),

#View advocate profile by client
    path('advocateprofileview/', views.advocateprofileview,name='advocateprofileview'),

# View more details of advocate by Client
    path('advocate_details/<id>/', views.advocate_details, name='advocate_details'),

#Add Case Details by client
    path('addcasedetails/', views.addcasedetails, name='addcasedetails'),

# View Status Updated by Advocate and Amount to be paid
    path('viewstatusamount/', views.viewstatusamount, name='viewstatusamount'),
    path('confirmamount/', views.confirmamount, name='confirmamount'),

    # path('clientsittingdetails/', views.clientsittingdetails, name='clientsittingdetails'),
    # path('clientsittingdetails/<int:casedetailsid>/', views.clientsittingdetails, name='clientsittingdetails'),
   path('clientsittingdetails/<int:casedetailsid>/', views.clientsittingdetails, name='clientsittingdetails'),
    path('view_case_status/', views.view_case_status, name='view_case_status'),

   path('card/', views.card,name='card'),

    path('view_case_status/', views.view_case_status, name='view_case_status'),

    ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
