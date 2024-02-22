from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse
from adminapp.models import *
from guestapp.models import *
from clientapp.models import *
from django.template import loader


# Create your views here.
def advocatehome(request):
    return render(request, "advocate/advhome.html")


# ...............................................
# UPDATE ADVOCATE PROFILE by Advocate
def advocateprofile(request):
    if "logid" in request.session:
        if request.method == 'POST':
            adv = Advocate()
            advocatename = request.POST.get('advocatename')
            emailid = request.POST.get('email')
            contactnumber = request.POST.get('contact')
            # casetype= Casetype.objects.get(casetypeid=request.POST.get('castddl'))
            # return HttpResponse(casetype)
            # location=Location.objects.get(locationid=request.POST.get('locddl'))
            licence = request.POST.get('license')
            experience = request.POST.get('experience')
            licencenumber = request.POST.get('licencenumber')

            adv = Advocate.objects.get(loginid=request.session["logid"])
            adv.advocatename = advocatename
            adv.emailid = emailid
            adv.contactnumber = contactnumber
            adv.experience = experience
            adv.licensenumber = licencenumber
            adv.save()
            return HttpResponse("Profile Updated Successfully")

        loginid = request.session['logid']
        # return HttpResponse(login_id)
        adv = Advocate.objects.get(loginid_id=loginid)
        return render(request, "advocate/updateadvocateprofile.html", {'adv': adv})
    else:
        return render(request, "guest/guestlogin.html")


# VIEW ADVOCATE PROFILE in Advocate Homepage
def viewadvocateprofile(request):
    if "logid" in request.session:
        loginid = request.session['logid']
        adv = Advocate.objects.get(loginid_id=loginid)
        return render(request, "advocate/advocateprofile.html", {'adv': adv})
    else:
        return render(request, "guest/guestlogin.html")


def viewcasedetails(request):
    advocate = Advocate.objects.get(loginid=request.session["logid"])
    caselist = Casedetails.objects.filter(advocateid=advocate)
    if request.method == 'POST':
        casedetails_id = request.POST.get('casedetails_id')
        status = request.POST.get('status')
        amount = request.POST.get('amount')
        caserequest = Casedetails.objects.get(casedetailsid=casedetails_id)
        caserequest.requeststatus = status
        caserequest.amount = amount
        caserequest.save()
        # return redirect('request,viewcasedetails')
    return render(request, "advocate/casedetails.html", {'caselist': caselist})


def confirmedcases(request):
    advocate = Advocate.objects.get(loginid=request.session["logid"])
    cases = Casedetails.objects.filter(advocateid=advocate, requeststatus='Confirmed')
    return render(request, 'advocate/confirmedcases.html', {'cases': cases})


# def addsitting(request, casedetailsid):
#     if request.method == 'POST':
#         casedetailsid = request.POST.get('casedetailsid')
#         casedetails = Casedetails.objects.get(casedetailsid=casedetailsid)
#         advocate = Advocate.objects.get(loginid=request.session["logid"])
#         sittingamount = request.POST.get('sittingamount')
#         submitedate = request.POST.get('submitedate')
#         sittingdescription = request.POST.get('sittingdescription')
#         sitting = Sitting.objects.create(
#             sittingamount=sittingamount,
#             casedetailsid=casedetails,
#             advocateid=advocate,
#             clientid=casedetails.clientid,
#             submitedate=submitedate,
#             sittingdescription=sittingdescription
#         )
#         return redirect('request,confirmedcases')
#     else:
#         # Handle the GET request

#         return render(request, 'advocate/addsitting.html')
# def addsitting(request, casedetailsid):
#     casedetails = Casedetails.objects.get(casedetailsid=casedetailsid)
#     if request.method == 'POST':
#         advocate = Advocate.objects.get(loginid=request.session["logid"])
#         sittingamount = request.POST.get('sittingamount')
#         submitedate = request.POST.get('submitedate')
#         sittingdescription = request.POST.get('sittingdescription')
#         sitting = Sitting.objects.create(
#             sittingamount=sittingamount,
#             casedetailsid=casedetails,
#             advocateid=advocate,
#             clientid=casedetails.clientid,
#             submitedate=submitedate,
#             sittingdescription=sittingdescription
#         )
#         return redirect('confirmedcases')
#     else:
#         # Handle the GET request
#         context = {'casedetails': casedetails}
#         return render(request, 'advocate/addsitting.html', context)

# def addsitting(request, casedetailsid):
#     casedetails = Casedetails.objects.get(casedetailsid=casedetailsid)
#     if request.method == 'POST':
#         advocate = Advocate.objects.get(loginid=request.session["logid"])
#         sittingamount = request.POST.get('sittingamount')
#         submitedate = request.POST.get('submitedate')
#         sittingdescription = request.POST.get('sittingdescription')
#         sitting = Sitting.objects.create(
#             sittingamount=sittingamount,
#             casedetailsid=casedetails,
#             advocateid=advocate,
#             clientid=casedetails.clientid,
#             submitedate=submitedate,
#             sittingdescription=sittingdescription
#         )
#         sittingpayment = SittingPayment.objects.create(
#             sittingid=sitting,
#             paymentdescription='Sitting payment',
#             paymentdate=submitedate,
#             paymentstatus='Pending'
#         )
#         return redirect('confirmedcases')
#     else:
#         # Handle the GET request
#         context = {'casedetails': casedetails}
#         return render(request, 'advocate/addsitting.html', context)
def addsitting(request, casedetailsid):
    casedetails = Casedetails.objects.get(casedetailsid=casedetailsid)
    if request.method == 'POST':
        advocate = Advocate.objects.get(loginid=request.session["logid"])
        sittingamount = request.POST.get('sittingamount')
        submitedate = request.POST.get('submitedate')
        sittingdescription = request.POST.get('sittingdescription')
        sitting = Sitting.objects.create(
            sittingamount=sittingamount,
            casedetailsid=casedetails,
            advocateid=advocate,
            clientid=casedetails.clientid,
            submitedate=submitedate,
            sittingdescription=sittingdescription
        )
        sittingpayment = SittingPayment.objects.create(
            sittingid=sitting,
            paymentdescription='Sitting payment',
            paymentdate=submitedate,
            paymentstatus='Pending'
        )
        return redirect('confirmedcases')
    else:
        sittings = Sitting.objects.filter(casedetailsid=casedetails)
        context = {'casedetails': casedetails, 'sittings': sittings}
        return render(request, 'advocate/addsitting.html', context)


def sittings(request):
    advocate = Advocate.objects.get(loginid=request.session["logid"])
    sittings = Sitting.objects.filter(advocateid=advocate, sittingpayment__paymentstatus='Pending')
    return render(request, 'advocate/sittings.html', {'sittings': sittings})


def confirmpayment(request, sittingid):
    print("confirmpayment view called")
    sitting = Sitting.objects.get(sittingid=sittingid)
    sittingpayment = SittingPayment.objects.get(sittingid=sitting)
    sittingpayment.paymentstatus = "Paid"
    sittingpayment.save()
    # sittingpayment = sitting.sittingpayment

    return redirect('sittings')


def viewcasedetails2(request):
    advocate = Advocate.objects.get(loginid=request.session["logid"])
    caselist = Casedetails.objects.filter(advocateid=advocate).order_by('clientid__clientname')
    return render(request, "advocate/updatecasestatus.html", {'caselist': caselist})



def updatecasestatus(request):
    if request.method == 'POST':
        casedetails_id = request.POST.get('casedetails_id')
        status = request.POST.get('status')
        nexthearingdate = request.POST.get('nexthearingdate') # new line
        caserequest = Casedetails.objects.get(casedetailsid=casedetails_id)
        casestatus = Cases.objects.create(
            advocateid=caserequest.advocateid,
            clientid=caserequest.clientid,
            casedetailsid=caserequest, # added this line
            statusdescription=status,
            nextdate=nexthearingdate, # new line
            updateddate=datetime.date.today() # modified this line
        )
        caserequest.requeststatus = 'Completed'
        caserequest.save()
        return redirect('advocatehome')
    else:
        return render(request, "guest/guestlogin.html")

# def viewcasedetails(request):
#     advocate = Advocate.objects.get(loginid=request.session["logid"])
#     caselist = Casedetails.objects.filter(advocateid=advocate).order_by('clientid__clientname')
#     if request.method == 'POST':
#         casestatus_id = request.POST.get('casestatus_id')
#         status = request.POST.get('status')
#         casestatus = Casestatus.objects.get(casestatusid=casestatus_id)
#         casestatus.statusdescription = status
#         casestatus.updateddate = date.today()
#         casestatus.save()
#         return redirect('viewcasedetails')
#     return render(request, "advocate/updatecasestatus.html", {'caselist': caselist})

