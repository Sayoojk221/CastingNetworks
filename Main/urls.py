from django.urls import path
from Main import views
urlpatterns = [
    path('',views.home,name='home'),
    path('userhome/',views.user_home),
    path('userlogin/',views.user_login),
    path('userregister/',views.user_register),
    path('companylogin/',views.company_login),
    path('companyregister/',views.company_register),
    path('userprofile/',views.user_profile),
]
