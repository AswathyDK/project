from django.shortcuts import render, redirect
from django.http import HttpResponse
from adminapp.models import *
from guestapp.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def clienthome(request):
    return render(request, "client/clienthome.html")


def advocateprofileview(request):
    cb = Casetype.objects.all()
    # cb=Casetype.objects.filter(casetypeid=id)
    return render(request, "client/advocateprofileview.html", {'cb': cb})


def casetypeadvocates(request):
    if request.method == 'POST':
        casetype_id = request.POST.get('ddlcasetype')
        request.POST.get('ddlcasetype')
        request.session['casetype']=casetype_id
        casetype = Casetype.objects.get(casetypeid=casetype_id)
        advocates = Advocate.objects.filter(casetypeid=casetype)
        # for adv in advocates:
        #     return HttpResponse(adv.photo)
        # return HttpResponse(advocates )
        return render(request, "client/card.html", {'advocates': advocates})
#view advocate
    casetypes = Casetype.objects.all()
    return render(request, "client/casetypeadvocates.html", {'casetypes': casetypes})


def advocate_details(request,id):
    advocate = Advocate.objects.get(advocateid=id)
    request.session['advocateid']=id
    return render(request, "client/advocatedetails.html", {'advocate': advocate})


def addcasedetails(request):
    if request.method == 'POST':
        # return HttpResponse("rose")
        cli = Client.objects.get(loginid_id=request.session['logid'])
        # return HttpResponse(cli.clientid)
        advocateid = request.POST.get('advocateid')
        casetypeid = request.POST.get('casetypeid')
        # clientid = request.POST.get('clientid')
        cl = Client.objects.get(clientid=cli.clientid)
        ad = Advocate.objects.get(advocateid=request.session['advocateid'])
        ca = Casetype.objects.get(casetypeid=request.session['casetype'])

        casetitle = request.POST.get('casetitle')
        description = request.POST.get('description')
        requeststatus = request.POST.get('requeststatus')
        filedetails = request.FILES.get('filedetails')
        amount = request.POST.get('amount')
        submitedate = request.POST.get('submitedate')
        Casedetails.objects.create(
            advocateid_id=ad.advocateid,
            casetypeid_id=ca.casetypeid,
            clientid_id=cl.clientid,
            casetitle=casetitle,
            description=description,
            requeststatus='requested',
            filedetails=filedetails,
            amount='0',
            submitedate=submitedate
        )
        return render(request, "client/addcasedetailes.html")
    advocates = Advocate.objects.get(advocateid=request.session['advocateid'])
    casetypes = Casetype.objects.get(casetypeid=request.session['casetype'])
    return render(request, "client/addcasedetailes.html", {'advocates': advocates, 'casetypes': casetypes})
    advocates=Advocate.objects.all()
    casetypes=Casetype.objects.all()
    client=Client.objects.all()
    return render(request, "client/addcasedetailes.html", {'advocates': advocates, 'casetypes': casetypes,'client':Clients})
def viewstatusamount(request):
    client = Client.objects.get(loginid=request.session["logid"])
    caselist = Casedetails.objects.filter(clientid_id=client)

    # caselist = Casedetails.objects.filter(clientid_id=client)
    return render(request, "client/viewstatusamount.html", {'caselist': caselist})


def confirmamount(request):
    if request.method == 'POST':
        casedetailsid = request.POST.get('casedetailsid')
        casedetails = Casedetails.objects.get(casedetailsid=casedetailsid)
        casedetails.requeststatus = 'Confirmed'
        casedetails.save()

        # Send acknowledgement to advocate side (implementation depends on your use case)

        return redirect('viewstatusamount')


# view sitting details added by advocate
def clientsittingdetails(request, casedetailsid):
    casedetails = Casedetails.objects.get(casedetailsid=casedetailsid)
    sittings = Sitting.objects.filter(casedetailsid=casedetails)
    context = {'sittings': sittings, 'casedetails': casedetails}
    return render(request, 'client/clientsittingview.html', context)

def card(request):
    return render(request, "client/card.html")

#VIEW CASE STATUS UPDATED BY ADVOCATE AFTER APPEARING THE COURT

def view_case_status(request):
    if "logid" in request.session:
        loginid = request.session['logid']
        client = Client.objects.get(loginid_id=loginid)
        casestatus = Cases.objects.filter(clientid=client)
        return render(request, "client/casestatus.html", {'casestatus': casestatus})
    else:
        return render(request, "guest/guestlogin.html")
