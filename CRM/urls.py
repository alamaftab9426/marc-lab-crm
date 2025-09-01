from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(("CRM_App.crmappurls","CRM_App"),namespace="CRM_App")),
    path('Customer/',include(("Customer.customerappurls","Customer"),namespace="Customer")),
    path('Adminapp/',include(("Adminapp.adminurls","Adminapp"),namespace="Adminapp")),
   
]

urlpatterns+=  static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
