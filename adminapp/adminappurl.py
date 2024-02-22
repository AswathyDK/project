from django.urls import path
from . import views
from . import views
# import ExportExcelLegal
from.views import ExportExcelLegal
from.views import ExportExcelLegal2


urlpatterns = [
    # Admin Home Page
    path('adminhome/', views.adminhome),

    path('district/', views.districtinsert),
    # Location add, view, edit, Delete
    path('location/', views.locationinsert, name="locationadd"),
    path('locationview/', views.locationview),
    path('editlocation/<id>/', views.editlocation, name="editlocation"),
    path('deletelocation/<id>/', views.deletelocation, name="deletelocation"),

    # casetype add,view,edit,delete
    path('casetype/', views.casetype, name="casetypeadd"),
    path('viewcasetype/', views.viewcasetype),
    path('editcasetype/<id>', views.editcasetype, name="editcasetype"),
    path('deletecasetype/<id>', views.deletecasetype, name="deletecasetype"),

    # confirm Advocate by Admin
    path('advocateviewnotconfirmed/', views.advocateviewnotconfirmed, name='advocateviewnotconfirmed'),
    path('advocateconfirm/<id>', views.advocateconfirm, name='advocateconfirm'),

    # view regitered client, edit, delete client

    path('clientregistrationview/', views.clientregistrationview, name='clientregistrationview'),
    path('editclientreg/<id>', views.editclientreg, name="editclientreg"),
    path('deleteclientreg/<id>', views.deleteclientreg, name="deleteclientreg"),
    path('export_excel/', ExportExcelLegal.as_view(), name='export_excel'),
    path('export_excel2/', ExportExcelLegal2.as_view(), name='export_excel2'),

]



