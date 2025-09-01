from django.urls import path
from  .  import views

urlpatterns = [
    path('',views.index,name='index'),
    path('AboutUS/',views.AboutUs,name='AboutUs'),
    path('ContactUs/',views.ContactUs,name='ContactUs'),
    path('Loginuser/',views.Loginuser,name='Loginuser'),
    path('Registration/',views.Registration,name='Registration'),
    path('allproduct/',views.allproduct,name='allproduct'),
]

