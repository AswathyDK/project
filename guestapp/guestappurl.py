from django.urls import path
from . import views

urlpatterns = [
    path('guesthome/', views.guesthome,name='guesthome'),
    # COMMON login to ADVOCATE, CLIENT, ADMIN From GuestSide
    path('llogin/', views.llogin, name='llogin'),

    # Advocate Registration-add,view,edit,delete
    path('advocatereg/', views.advocatereg, name='advocatereg'),
    path('registrationview/', views.registrationview, name='registrationview'),
    path('editadvocatereg/<id>', views.editadvocatereg, name="editadvocatereg"),
    path('deleteadvocatereg/<id>', views.deleteadvocatereg, name="deleteadvocatereg"),

    # Client Registration
    path('clientreg/', views.clientreg, name='clientreg'),

    # path('clientadvocateview/',views.clientadvocateview),
    path('base/', views.basehome),

]