from django.shortcuts import render,redirect,reverse
from . models import FarmerInfo,MerchantInfo,LoginInfo,Enquiry
import datetime
from adminapp.models import News

def index(request):
    ns=News.objects.all()
    return render(request,'index.html',{'ns':ns})
def about(request):
    ns=News.objects.all()
    return render(request,'about.html',{'ns':ns})
def farmerreg(request):
    ns = News.objects.all()
    return render(request,'farmerreg.html',{'ns':ns})
def merchantreg(request):
    ns = News.objects.all()
    return render(request,'merchantreg.html',{'ns':ns})
def login(request):
    ns = News.objects.all()
    return render(request,'login.html',{'ns':ns})
def contact(request):
    ns = News.objects.all()
    return render(request,'contact.html',{'ns':ns})
def freg (request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    aadhaarno=request.POST['aadhaarno']
    regdate=datetime.datetime.today()
    fi=FarmerInfo(name=name,gender=gender,address=address,contactno=contactno,aadhaarno=aadhaarno,regdate=regdate)
    fi.save()
    msg='You have registered successfully'
    return render(request,'farmerreg.html',{'msg':msg})
def mreg (request):
    name=request.POST['name']
    gender = request.POST['gender']
    firmname=request.POST['firmname']
    firmaddress=request.POST['firmaddress']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    aadhaarno=request.POST['aadhaarno']
    panno=request.POST['panno']
    gstno=request.POST['gstno']
    demand=request.POST['demand']
    regdate=datetime.datetime.today()
    mi=MerchantInfo(name=name,gender=gender,firmname=firmname,firmaddress=firmaddress,contactno=contactno,emailaddress=emailaddress,aadhaarno=aadhaarno,panno=panno,gstno=gstno,demand=demand,regdate=regdate)
    mi.save()
    msg='Merchant have registered successfuly'
    return render(request,'merchantreg.html',{'msg':msg})
def validate(request):
    userid=request.POST['userid']
    password=request.POST['password']
    try:
        obj=LoginInfo.objects.get(userid=userid,password=password)
        request.session['userid']=userid
        return redirect(reverse('adminapp:adminhome'))
    except:
        msg='Invalid User'
    return render(request,'login.html',{'msg':msg})
def saveenq(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enquirydate=datetime.datetime.today()
    eq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
    eq.save()
    msg='Your enquiry is Submitted'
    return render(request,'contact.html',{'msg':msg})
