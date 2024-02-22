from django.shortcuts import render
from django.http import HttpResponse
from adminapp.models import *
from guestapp.models import *
from clientapp.models import *
from django.template import loader
import xlwt
from django.views.generic import View

# Create your views here.
def adminhome(request):
    return render(request, "admin/adminhome.html")


# Create your views here.


# district insert

def districtinsert(request):
    return render(request, "admin/district.html")


def locationinsert(request):
    if request.method == 'POST':

        locationname = request.POST.get('locationname')
        d = District.objects.get(districtid=request.POST.get('ddldistrict'))
        if Location.objects.filter(locationname=locationname).exists():
            return HttpResponse("<script>alert('Duplicate..');window.location='Admin/location.html';</script>")
        loc_obj = Location()
        loc_obj.locationname = locationname
        loc_obj.districtid = d
        loc_obj.save()
        return HttpResponse("<script>alert('Insert..');window.location='Admin/location.html';</script>")
    dis = District.objects.all()
    return render(request, "admin/location.html", {'d': dis})


# locationview
def locationview(request):
    dis = Location.objects.all()
    return render(request, "admin/viewlocation.html", {'Location': dis})


# locationedit
def editlocation(request, id):
    if request.method == 'POST':
        lname = request.POST.get('locationname')
        loc = Location.objects.get(locationid=id)
        loc.locationname = lname
        loc.save()
        return locationview(request)
    else:
        dis = District.objects.all()
        loc = Location.objects.get(locationid=id)
        return render(request, "admin/editlocation.html", {'d': dis, 'loc': loc})


# location delete
def deletelocation(request, id):
    loc = Location.objects.get(locationid=id)
    loc.delete()
    return locationview(request)


# casetype
def casetype(request):
    if request.method == 'POST':
        casetype = request.POST.get('casetype')
        description = request.POST.get('Description')
        if Casetype.objects.filter(casetype=casetype).exists():
            return HttpResponse("<script>alert('Duplicate..');window.location='Admin/casetype.html';</script>")
        cas_obj = Casetype()
        cas_obj.casetype = casetype
        cas_obj.description = description
        cas_obj.save()
        return HttpResponse("<script>alert('Insert..');window.location='Admin/casetype.html';</script>")
    return render(request, "admin/casetype.html")


def viewcasetype(request):
    dis = Casetype.objects.all()
    return render(request, "admin/viewcasetype.html", {'Casetype': dis})


def editcasetype(request, id):
    if request.method == 'POST':
        cname = request.POST.get('casetype')
        cdis = request.POST.get('description')

        cas = Casetype.objects.get(casetypeid=id)
        cas.casetype = cname
        cas.description = cdis
        cas.save()
        return viewcasetype(request)
    else:
        cas = Casetype.objects.get(casetypeid=id)
        return render(request, "admin/editcasetype.html", {'cas': cas})


def deletecasetype(request, id):
    cas = Casetype.objects.get(casetypeid=id)
    cas.delete()
    return viewcasetype(request)


def advocateviewnotconfirmed(request):
    adv = Advocate.objects.select_related('loginid').filter(loginid__status='Not Confirmed')
    return render(request, 'guest/viewadvocatereg.html', {"adv": adv})


def advocateconfirm(request, id):
    if id:
        obj = Login.objects.get(loginid=id)
        # return HttpResponse(obj.status)
        obj.status = "Confirmed"
        obj.save()
    return advocateviewnotconfirmed(request)


def clientregistrationview(request):
    cli = Client.objects.all()
    return render(request, "guest/viewclientreg.html", {'cli': cli})


def editclientreg(request, id):
    if request.method == 'POST':
        clientname = request.POST.get('clientname')
        dist = District.objects.get(districtid=request.POST.get('dis'))
        loc = Location.objects.get(locationid=request.POST.get('locddl'))
        housename = request.POST.get('housename')
        pincode = request.POST.get('pincode')
        email = request.POST.get('emailid')
        contactnumber = request.POST.get('contactnumber')
        username = request.POST.get('username')
        password = request.POST.get('password')

        cnt = Client.objects.get(clientid=id)
        cnt.clientname = clientname
        cnt.district = dist
        cnt.locationname = loc
        cnt.housename = housename
        cnt.pincode = pincode
        cnt.email = email
        cnt.contactnumber = contactnumber
        # cnt.username = username
        # cnt.password = password
        cnt.save()
        return clientregistrationview(request)
    else:

        cnt = Client.objects.get(clientid=id)
        # dis_obj = District()
        dist = District.objects.all()
        # loc_obj = Location()
        loc = Location.objects.all()
        return render(request, "guest/editclientreg.html", {'cnt': cnt, 'dist': dist, 'loc': loc})


def deleteclientreg(request, id):
    cnt = Client.objects.get(clientid=id)
    cnt.delete()
    return clientregistrationview(request)

class ExportExcelLegal(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="advocatelist.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['advocatename', 'emailid', 'contactnumber', 'license', 'experience','licensenumber']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        queryset = Advocate.objects.all().values_list('advocatename', 'emailid', 'contactnumber', 'license', 'experience','licensenumber')
        for row in queryset:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

class ExportExcelLegal2(View):
        def get(self, request):
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="clientlist.xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sheet1')

            # Define the column headings
            row_num = 0
            columns = ['clientname', 'housename', 'pincode', 'contactnumber', 'emailid']
            for col_num, column_title in enumerate(columns):
                ws.write(row_num, col_num, column_title)

            # Query the data from your model, and write it to the worksheet
            queryset = Client.objects.all().values_list('clientname', 'housename', 'pincode', 'contactnumber', 'emailid')
            for row in queryset:
                row_num += 1
                for col_num, cell_value in enumerate(row):
                    ws.write(row_num, col_num, cell_value)

            wb.save(response)
            return response
