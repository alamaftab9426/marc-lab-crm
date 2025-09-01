from django.shortcuts import render , redirect
from . models import Enquiry , Customer , Login 
# For sending Mail
from django.conf import settings
from django.core.mail import send_mail
# For importing date and time 
import datetime
# Exception Handling
from django.core.exceptions import ObjectDoesNotExist
from Adminapp . models import Product

# Create your views here.

def index(request):
    return render(request,"index.html")

def AboutUs(request):
    return render(request,"aboutus.html")

def ContactUs(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        subject1 = request.POST.get('subject')
        message = request.POST.get('message')
        posted_date = datetime.datetime.now()
        data = Enquiry(name=name,contact=contact,email=email,subject=subject1,message=message,posted_date=posted_date)
        data.save()
        
        # subject = 'Enquiry Form' 
        # message = f'Hi {name}, thank you for your enquiry your message subject is {subject1} and your message is {message}'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [email, ]
        # send_mail( subject, message, email_from, recipient_list )

        return render(request,"contactus.html",{"msg":"Succesfully Send Your Query"})
    
    return render(request,"contactus.html")

def Loginuser(request):
    
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        try:
             user1 = Login.objects.get(userid=username,password=password)
             if user1 is not None:
                 if user1.usertype=="Customer":
                    request.session['userid'] = username
                    return redirect("Customer:customerhome")
                 elif user1.usertype=="Admin":
                     request.session['adminid']=username
                     return redirect("Adminapp:adminhome")
                     
        except ObjectDoesNotExist:
            return render(request,"login.html",{"msg":"Invalid Username or Password !!"})
            
    return render(request,"login.html")


def Registration(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        password = request.POST.get('password')
        reg_date = datetime.datetime.now()
        
        data = Customer(name=name,email=email,address=address,contactno=contact,gender=gender,reg_date=reg_date)
        data.save()
        log = Login(userid=email,password=password,usertype="Customer")
        log.save()
        
        return render(request,"login.html",{"reg_msg":"Registered Successfully!!! \n Please Login to Continue"})   
    return render(request,"registration.html")


def allproduct(request):
    pro = Product.objects.all()
    return render(request,"allproducts.html",locals())