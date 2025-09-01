from django.shortcuts import render ,redirect
from django.views.decorators.cache import cache_control
from CRM_App.models import Customer , Enquiry
from Customer .models import Response
from .models import Product
# Create your views here.

@cache_control(no_cache=True , must_revalidate=True , no_store=True)

def adminhome(request):
    try:
        if request.session['adminid']!=None:
            adminid = request.session['adminid']
            data = Customer.objects.all()
            data2 = Enquiry.objects.all()
            pro = Product.objects.all()
            com = Response.objects.filter(responsetype="Complains")
            fed = Response.objects.filter(responsetype="Feedback")
            total_enquiry = data2.count()
            total_user = data.count()
            total_fed = fed.count()
            total_com = com.count()
            total_pro = pro.count()
            adminid = request.session['adminid']
            feedback = Response.objects.filter(responsetype="Feedback").order_by('-id')[:3]
            return render(request,"adminhome.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")
    
def Logout(request):
    try:
        del request.session['adminid']
    except KeyError:
        return redirect("CRM_App:Loginuser")
    return redirect("CRM_App:Loginuser")

def Viewcustomer(request):
    try:
        if request.session['adminid']!=None:
            adminid = request.session['adminid']
            data = Customer.objects.all()
            return render(request,"viewcustomer.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")
    
    
def ViewEnquiry(request):
    try:
        if request.session['adminid']!=None:
            adminid = request.session['adminid']
            data = Enquiry.objects.all()
            return render(request,"viewenquiries.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")
    
def delquery(request,id):
    try:
        if request.session['adminid']!=None:
            adminid = request.session['adminid']
            data = Enquiry.objects.get(id=id)
            data.delete()
            return redirect("Adminapp:ViewEnquiry")
    except KeyError:
        return redirect("CRM_App:Loginuser")
        
@cache_control(no_cache=True , must_revalidate=True , no_store=True)      

def product(request):
    try:
        if request.session['adminid']!=None:
            adminid = request.session['adminid']
            products = Product.objects.all()
            if request.method == "POST":
                pname = request.POST.get('pname')
                mfgdate = request.POST.get('mfgdate')
                expdate = request.POST.get('expdate')
                price = request.POST.get('price')
                productpic = request.FILES.get('productpic')
                data = Product(product_name=pname,mfg_date=mfgdate,exp_date=expdate,price=price,product_pic=productpic)
                data.save()
                msg="Succesfully Added Product !!"
                return render(request,"product.html",locals())
            return render(request,"product.html",locals())
    except KeyError:
       return redirect("CRM_App:Loginuser")
    
    
@cache_control(no_cache=True , must_revalidate=True , no_store=True)   

def Viewcomplain(request):
    try:
        if request.session['adminid']!=None:
            adminid = request.session['adminid']
            com = Response.objects.filter(responsetype="Complains")
            return render(request,"complain.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")
    
@cache_control(no_cache=True , must_revalidate=True , no_store=True)   

def Viewfeedback(request):
    try:
        if request.session['adminid']!=None:
            adminid = request.session['adminid']
            fed = Response.objects.filter(responsetype="Feedback")
            return render(request,"feedback.html",locals())
    except KeyError:
        return redirect("CRM_App:Loginuser")

    
def delresponse(request,id):
    try:
        if request.session['adminid']!=None:
            adminid = request.session['adminid']
            data = Response.objects.get(id=id)
            data.delete()
            return redirect("Adminapp:adminhome")
    except KeyError:
        return redirect("CRM_App:Loginuser")