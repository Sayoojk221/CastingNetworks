from django.urls import path
from Main import views
urlpatterns = [
    path('',views.home,name='home'),
    path('adminlogout/',views.admin_logout),
    path('userhome/',views.user_home),
    path('companyhome/',views.company_home),
    path('userlogin/',views.user_login),
    path('userregister/',views.user_register),
    path('companylogin/',views.company_login),
    path('companyregister/',views.company_register),
    path('companylogout/',views.company_logout),
    path('companyprofile/',views.company_profile),
    path('companyimageupload/',views.companyimage_upload),
    path('usercastcallrequestapprove/',views.usercastcallrequest_approve),
    path('userprofile/',views.user_profile),
    path('userimageupload/',views.userimage_upload),
    path('userlogout/',views.user_logout),
    path('castcallregister/',views.castcall_register),
    path('filmpromotion/',views.film_promotion),
    path('tags/',views.film_tags),
    path('castcallview/',views.castcall_view),
    path('castcallapply/',views.castcall_apply),
    path('adminuserview/',views.adminuser_view),
    path('admintotaluserview/',views.admintotaluser_view),
    path('admincompanyview/',views.admincompany_view),
    path('admintotalcompanyview/',views.admintotalcompany_view),
    path('admincastview/',views.admincast_view),
    path('promotionvideo/',views.promotion_video),
    path('usertotalcastcall/',views.usertotalcast_call),
    path('castcalldelete/',views.castcall_delete),



]
