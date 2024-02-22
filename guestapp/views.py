from django.shortcuts import render
from django.http import HttpResponse
from adminapp.models import *
from guestapp.models import *
from clientapp.models import *
from django.template import loader


# Create your views here.
def guesthome(request):
    return render(request, "guest/ghome.html")


def llogin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if Login.objects.filter(username=username, password=password).exists():
            # return HttpResponse("hi")

            loginobj = Login.objects.get(username=username, password=password)
            request.session['uname'] = loginobj.username
            request.session['logid'] = loginobj.loginid
            role = loginobj.role
            # return HttpResponse(role)
            if role == "admin":
                # return HttpResponse("HI")
                return render(request, 'admin/adminhome.html')
            elif role == "Client":
                # return HttpResponse("HI")
                # my_object.field_name=my_object.field_name.strip()
                return render(request, 'client/clienthome.html')
            elif role == "advocate":
                # return HttpResponse(loginobj.status)
                if loginobj.status == "Confirmed":
                    return render(request, 'advocate/advocatehome.html')
                else:
                    # return render(request, "GuestUsers_old/Login_old.html", {"error": "Pls wait for confirmation"})
                    return render(request, "guest/login.html", {"error": "Pls wait for confirmation"})
            else:
                return HttpResponse("Hai")
        else:
            context = {"error": "incorrect user name or password"}
            return render(request, "guest/ghome.html", context)
    else:
        return render(request, "guest/login.html")


def advocatereg(request):
    if request.method == 'POST':

        advocatename = request.POST.get('advocatename')
        emailid = request.POST.get('email')
        contactnumber = request.POST.get('contact')
        casetype = Casetype.objects.get(casetypeid=request.POST.get('castddl'))
        # return HttpResponse(casetype)
        location = Location.objects.get(locationid=request.POST.get('locddl'))
        licence = request.POST.get('license')
        experience = request.POST.get('experience')
        licencenumber = request.POST.get('licencenumber')

        username = request.POST.get('username')
        password = request.POST.get('password')
        '''if advocatereg.objects.filter(advocateid=advocatename).exists():
            return HttpResponse("<script>alert('Duplicate..');window.location='guest/advocatereg.html';</script>")
        '''

        adv1_obj = Login()
        adv1_obj.username = username
        adv1_obj.password = password
        adv1_obj.role = "advocate"
        adv1_obj.save()

        adv_obj = Advocate()
        adv_obj.advocatename = advocatename
        adv_obj.emailid = emailid
        adv_obj.contactnumber = contactnumber
        adv_obj.casetypeid = casetype
        adv_obj.locationid = location
        adv_obj.license = licence
        adv_obj.experience = experience
        adv_obj.licensenumber = licencenumber
        adv_obj.loginid = adv1_obj
        if len(request.FILES) != 0:
            sphoto = request.FILES['photo']
        else:
            sphoto = 'images/default.jpeg'
        adv_obj.photo = sphoto
        if len(request.FILES) != 0:
            slicense = request.FILES['license']
        else:
            slicense = 'images/default.jpeg'
        adv_obj.license = slicense
        adv_obj.save()

    case_obj = Casetype()
    case = Casetype.objects.all()
    loc_obj = Location()
    loc = Location.objects.all()
    return render(request, "guest/advocatereg.html", {'case': case, 'loc': loc})


def registrationview(request):
    dl = Advocate.objects.all()
    return render(request, "Guest/viewadvocatereg.html", {'dl': dl})


def editadvocatereg(request, id):
    if request.method == 'POST':
        advocatename = request.POST.get('advocatename')
        loc = Location.objects.get(locationid=request.POST.get('locddl'))
        experience = request.POST.get('experience')
        licencenumber = request.POST.get('licencenumber')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        adv = Advocate.objects.get(advocateid=id)
        adv.advocatename = advocatename
        adv.locationname = loc
        adv.experience = experience
        adv.licensenumber = licencenumber
        adv.emailid = email
        adv.contactnumber = contact

        adv.save()
        return registrationview(request)
    else:
        adv = Advocate.objects.get(advocateid=id)
        loc = Location.objects.all()
        return render(request, "guest/editadvocatereg.html", {'adv': adv, 'loc': loc})


def deleteadvocatereg(request, id):
    adv = Advocate.objects.get(advocateid=id)
    adv.delete()


# def login(request):
#     if request.method=='POST':

#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         role = request.POST.get('role')

#         log_obj = Login()
#         log_obj.username = username
#         log_obj.password = password
#         log_obj.role = role
#         log_obj.save()
#     log = Login.objects.all()
#     return render(request, "guest/login.html",{'log':log})

def clientreg(request):
    if request.method == 'POST':
        clientename = request.POST.get('clientname')
        district = District.objects.get(districtid=request.POST.get('dis'))
        location = Location.objects.get(locationid=request.POST.get('locddl'))
        housename = request.POST.get('housename')
        pincode = request.POST.get('pincode')
        emailid = request.POST.get('emailid')
        contactnumber = request.POST.get('contactnumber')
        username = request.POST.get('username')
        password = request.POST.get('password')

        cln_obj = Login()
        cln_obj.username = username
        cln_obj.password = password
        cln_obj.role = "Client"
        cln_obj.save()

        clnt_obj = Client()
        clnt_obj.clientname = clientename
        clnt_obj.districtid = district
        clnt_obj.locationid = location
        clnt_obj.housename = housename
        clnt_obj.pincode = pincode
        clnt_obj.emailid = emailid
        clnt_obj.contactnumber = contactnumber
        clnt_obj.loginid = cln_obj
        clnt_obj.save()

    dis_obj = District()
    dis = District.objects.all()
    loc_obj = Location()
    loc = Location.objects.all()
    return render(request, "guest/clientreg.html", {'dis': dis, 'loc': loc})
    return render(request, "guest/clientreg.html")

def basehome(request):
    return render(request, "guest/base.html")












