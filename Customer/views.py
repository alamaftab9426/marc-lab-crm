from django.shortcuts import render ,redirect
from django.views.decorators.cache import cache_control
from CRM_App.models import Customer , Login
from .models import Response
from Adminapp . models import Product
import datetime

# Create your views here.
@cache_control(no_cache=True , must_revalidate=True , no_store=True)

def customerhome(request):
    try:
        if request.session['userid']!=None:
            userid = request.session['userid']
            User = Customer.objects.get(email=userid)
            return render(request,"customerhome.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")
    
def logout(request):
    try:
        del request.session['userid']
    except KeyError:
        return redirect("CRM_App:Loginuser")
    return redirect("CRM_App:Loginuser")

def response(request):
    try:
        if request.session['userid']!=None:
            userid = request.session['userid']
            User = Customer.objects.get(email=userid)
            
            if request.method == "POST":
               name =  User.name
               contactno = User.contactno
               email = userid
               responsetype = request.POST.get("restype") 
               subject = request.POST.get("subject") 
               restext = request.POST.get("restext") 
               posteddate = datetime.datetime.now()
               
               data = Response(name=name,contactno=contactno,email=email,responsetype=responsetype,subject=subject,responsetext=restext,posteddate=posteddate)
               data.save()
               savemsg = "Your Response has been sent !!!"
            return render(request,"response.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")
    
    
@cache_control(no_cache=True , must_revalidate=True , no_store=True)

def profile(request):
    try:
        if request.session['userid']!=None:
            userid = request.session['userid']
            User = Customer.objects.get(email=userid)
            if request.method == "POST":
                name = request.POST.get("name")
                gender = request.POST.get("gender")
                contactno = request.POST.get("contact")
                address = request.POST.get("address")
                Customer.objects.filter(email=userid).update(name=name,gender=gender,contactno=contactno,address=address)
                msg = "Infromation Updated Successfully !! "
                return redirect('Customer:profile')
                
            return render(request,"viewprofile.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")
    
@cache_control(no_cache=True , must_revalidate=True , no_store=True)

def cusproduct(request):
    try:
        if request.session['userid']!=None:
            userid = request.session['userid']
            User = Customer.objects.get(email=userid)
            pro = Product.objects.all()
            return render(request,"cus_product.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")

@cache_control(no_cache=True , must_revalidate=True , no_store=True)

def changepass(request):
    try:
        if request.session['userid']!=None:
            userid = request.session['userid']
            User = Customer.objects.get(email=userid)
            if request.method == "POST":
                password = request.POST.get("pass")
                cpassword = request.POST.get("cpass")
                if password == cpassword:
                    Login.objects.filter(userid=userid).update(password=password)
                    msg = "Password Updated Successfully !!! "
                else:
                    msg = "Password Does not match !!!"
                
            return render(request,"channgepass.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")
    