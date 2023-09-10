from django.shortcuts import render, redirect
from fmiapp.models import FarmerInfo, MerchantInfo, LoginInfo, Enquiry
from . models import Booking, News, mBooking
import datetime
# adminapp view use to admin work
def adminhome(request):
    try:
       if request.session['userid']:
           ns=News.objects.all()
           return render(request,'adminhome.html',{'ns':ns})
    except:
        return render(request,'login.html')
def enquiries(request): #enquiriesviews
    try:
        if request.session['userid']:
            enq=Enquiry.objects.all()
            return render(request,'enquiries.html',{'enq':enq})
    except:
        return render(request,'login.html')
def booking(request):
    try:
        if request.session['userid']:
            fi=FarmerInfo.objects.all()
            return render(request,'booking.html',{'fi':fi})
    except:
        return render(request,'login.html')
def mbooking(request):
    try:
        if request.session['userid']:
            mi = MerchantInfo.objects.all()
            return render(request, 'mbooking.html', {'mi': mi})
    except:
        return render(request, 'login.html')

def purchase(request):
    try:
        if request.session['userid']:
            bk=Booking.objects.all()
            return render(request,'purchase.html',{'bk':bk})
    except:
        return render(request,'login.html')
def mac(request):
    try:
        if request.session['userid']:
            ma=mBooking.objects.all()
            return render(request,'mac.html',{'ma':ma})
    except:
        return render(request,'login.html')
def changepassword(request):
    try:
        if request.session['userid']:
            return render(request,'changepassword.html')
    except:
        return render(request,'login.html')

def logout(request):
        request.session['userid']=None
        return render(request,'login.html')

def book(request,ano):
    fi=FarmerInfo.objects.get(aadhaarno=ano)
    return render(request,'book.html',{'fi':fi})

def mbook(request,m):
    mi=MerchantInfo.objects.get(aadhaarno=m)
    return render(request,'mbook.html',{'mi':mi})

def pbook(request):
    name=request.POST['name']
    address=request.POST['address']
    contactno=request.POST['contactno']
    aadhaarno=request.POST['aadhaarno']
    noofpacket=int(request.POST['noofpacket'])
    duration=int(request.POST['duration'])
    rate=int(request.POST['rate'])
    advance=int(request.POST['advance'])
    totalamt=noofpacket*duration*rate
    restamt=totalamt-advance
    bookingdate=datetime.datetime.today()
    b = Booking(name=name,address=address,contactno=contactno,aadhaarno=aadhaarno,noofpacket=noofpacket,duration=duration,rate=rate,advance=advance,totalamt=totalamt,restamt=restamt,bookingdate=bookingdate)
    b.save()
    msg='Booking is completed'
    return redirect('adminapp:booking')

def mlook(request):
    name=request.POST['name']
    firmname=request.POST['firmname']
    firmaddress=request.POST['firmaddress']
    contactno=request.POST['contactno']
    aadhaarno=request.POST['aadhaarno']
    panno=request.POST['panno']
    gstno=request.POST['gstno']
    demand=request.POST['demand']
    ninkg=int(request.POST['ninkg'])
    rate=int(request.POST['rate'])
    advance=int(request.POST['advance'])
    totalamt=ninkg*rate
    restamt=totalamt-advance
    bookingdate=datetime.datetime.today()
    b = mBooking(name=name,firmname=firmname,firmaddress=firmaddress,contactno=contactno,aadhaarno=aadhaarno,panno=panno,gstno=gstno,demand=demand,ninkg=ninkg,rate=rate,advance=advance,totalamt=totalamt,restamt=restamt,bookingdate=bookingdate)
    b.save()
    msg='Booking is completed'
    return redirect('adminapp:mbooking')

def viewbook(request,ano):
    res=Booking.objects.get(aadhaarno=ano)
    return render(request,'viewbook.html',{'res':res})

def mview(request,m):
    res=mBooking.objects.get(aadhaarno=m)
    return render(request,'mview.html',{'res':res})

def deleteenq(request,id):
    e=Enquiry.objects.get(id=id)
    e.delete()
    return redirect('adminapp:enquiries')

def addnews(request):
    newstext=request.POST['newstext']
    newsdate=datetime.datetime.today()
    ns = News(newstext=newstext,newsdate=newsdate)
    ns.save()
    return redirect('adminapp:adminhome')

def deletenews(request,id):
    ns=News.objects.get(id=id)
    ns.delete()
    return redirect('adminapp:adminhome')
def changepwd(request,):
    op=request.POST['op']
    np=request.POST['np']
    cp=request.POST['cp']
    msg='Message='
    if np!=cp:
        msg=msg+'New password is not matched with comfirm Password'
        return render(request,'changepassword.html',{'msg':msg})
    userid=request.session['userid']
    try:
        obj=LoginInfo.objects.get(userid=userid,password=op)
        LoginInfo.objects.filter(userid=userid).update(password=np)
        return redirect('adminapp:logout')
    except:
        msg=msg+'Old password is not match'
    return render(request,'changepassword.html',{'msg':msg})

def pay(request,ano):
    obj=Booking.objects.get(aadhaarno=ano)
    return render(request,'pay.html',{'obj':obj})

def macpay(request,mc):
    mac=mBooking.objects.get(aadhaarno=mc)
    return render(request,'macpay.html',{'mac':mac})

def paid(request):
    aadhaarno=request.POST['aadharno']
    restamt=int(request.POST['restamt'])
    payamt=int(request.POST['payamt'])
    restamt=restamt-payamt
    Booking.objects.filter(aadhaarno=aadhaarno).update(restamt=restamt)
    return redirect('adminapp:purchase')
def mpaid(request):
    aadhaarno=request.POST['aadhaarno']
    restamt=int(request.POST['restamt'])
    payamt=int(request.POST['payamt'])
    restamt=restamt-payamt
    mBooking.objects.filter(aadhaarno=aadhaarno).update(restamt=restamt)
    return redirect('adminapp:mac')

