from django.urls import path
from  .  import views

urlpatterns = [
    path('customerhome/',views.customerhome,name="customerhome"),
    path('logout/',views.logout,name="logout"),
    path('response/',views.response,name="response"),
    path('profile/',views.profile,name="profile"),
    path('cusproduct/',views.cusproduct,name="cusproduct"),
    path('changepass/',views.changepass,name="changepass"),
    
]