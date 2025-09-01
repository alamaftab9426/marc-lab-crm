from django.urls import path
from  .  import views

urlpatterns = [
     path('adminhome/',views.adminhome,name="adminhome"),
     path('Logout/',views.Logout,name="Logout"),
     path('Viewcustomer/',views.Viewcustomer,name="Viewcustomer"),
     path('ViewEnquiry',views.ViewEnquiry,name="ViewEnquiry"),
     path('delquery/<id>',views.delquery,name="delquery"),
     path('product/',views.product,name="product"),
     path('Viewfeedback/',views.Viewfeedback,name="Viewfeedback"),
     path('Viewcomplain/',views.Viewcomplain,name="Viewcomplain"),
     path('delresponse/<id>',views.delresponse,name="delresponse"),
    
]