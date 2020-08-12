from django.shortcuts import render,redirect
from Main.models import *

def admin(request):
    if request.session.has_key('admin-id'):
        return redirect('/admindashboard/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['pass']
            admin_details = Admin.objects.all().filter(username=username,password=password)
            for i in admin_details:
                request.session['admin-id']=i.id
            if admin_details:
                return redirect('/admindashboard/')

            else:
                return render(request,'admin/login.html')
        else:
            return render(request,'admin/login.html')

def admin_dashboard(request):
    if request.session.has_key('admin-id'):
        total_user = UserRegister.objects.all().filter(status='approve').count()
        total_company = FilmCompany.objects.all().filter(status='approve').count()
        total_castcall = CastRegister.objects.all().filter(status='approve').count()
        context = {'user':total_user,'company':total_company,'cast':total_castcall}
        return render(request,'admin/dashboard.html',context)
    else:
        return redirect('/admin/')

def admin_logout(request):
    if request.session.has_key('admin-id'):
        del request.session['admin-id']
        return redirect('/admin/')
    else:
        return redirect('/admin/')


def home(request):
    tag_id = request.GET.get('id')
    all_tags = Tags.objects.all()
    if tag_id:
        tagname = Tags.objects.filter(id=tag_id)
        castcall_details = CastRegister.objects.all().filter(tags=tag_id)
        context = {'castcall':castcall_details,'tagname':tagname,'tags':all_tags}
        return render(request,'base/home.html',context)
    else:
        castcall_details = CastRegister.objects.all()
        context = {'castcall':castcall_details,'tags':all_tags}
        return render(request,'base/home.html',context)

def user_home(request):
    tag_id = request.GET.get('id')
    all_tags = Tags.objects.all()
    if tag_id:
        user = request.session['user-id']
        booked_castcall_details = CastBooking.objects.all().filter(user_id=user).values('cast_id')
        total_booked_castcall_id = []
        for item in booked_castcall_details:
            for i in item:
                total_booked_castcall_id.append(item[i])
        tagname = Tags.objects.filter(id=tag_id)
        castcall_details = CastRegister.objects.all().filter(tags=tag_id)
        context = {'castcall':castcall_details,'total_id':total_booked_castcall_id,'tagname':tagname,'tags':all_tags}
        return render(request,'user/homepage.html',context)
    else:
        user = request.session['user-id']
        booked_castcall_details = CastBooking.objects.all().filter(user_id=user).values('cast_id')
        total_booked_castcall_id = []
        for item in booked_castcall_details:
            for i in item:
                total_booked_castcall_id.append(item[i])

        castcall_details = CastRegister.objects.all()
        context = {'castcall':castcall_details,'total_id':total_booked_castcall_id,'tags':all_tags}
        return render(request,'user/homepage.html',context)

def company_home(request):
    companyid = request.session['company-id']
    details = FilmCompany.objects.filter(id=companyid)
    context = {'details':details}
    return render(request,'company/companyhome.html',context)

def user_login(request):
    if request.session.has_key('user-id'):
        return redirect('/userhome/')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['pass']
            user_details = UserRegister.objects.all().filter(email=email,password=password,status='approve')
            for i in user_details:
                request.session['user-id']=i.id
            if user_details:
                return redirect('/userhome/')
            else:
                message = 'Invaild username and password!'
                return render(request,'user/login.html',{'message':message})
        else:
            return render(request,'user/login.html')

def user_register(request):
    if request.session.has_key('user-id'):
       return redirect('/userhome/')
    else:
        if request.method == 'POST':
            fullname = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['pass']
            user_details = UserRegister(profile_image='user/default.jpg',fullname=fullname,username=username,email=email,password=password,status='pending')
            user_details.save()
            return render(request,'user/login.html')
        else:
            return render(request,'user/register.html')

def user_profile(request):
    if request.session.has_key('user-id'):
        userid = request.session['user-id']
        user_details = UserRegister.objects.filter(id=userid)
        context = {'edit':user_details}
        if request.method == 'POST':
            fullname = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            address = request.POST['address']
            state = request.POST['state']
            phone = request.POST['phone']
            UserRegister.objects.filter(id=userid).update(fullname=fullname,username=username,email=email,address=address,state=state,phone_number=phone)
            return render(request,'user/profile.html',context)
        else:
            return render(request,'user/profile.html',context)
    else:
        return render(request,'user/login.html')

def company_profile(request):
    if request.session.has_key('company-id'):
        company = request.session['company-id']
        company_details = FilmCompany.objects.filter(id=company)
        context = {'details':company_details}
        if request.method == 'POST':
            companyname = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            FilmCompany.objects.all().filter(id=company).update(company_name=companyname,email=email,address=address,phone_number=phone)
            return render(request,'company/profile.html',context)
        else:
            return render(request,'company/profile.html',context)
    else:
        return render(request,'company/login.html')


def companyimage_upload(request):
    if request.session.has_key('company-id'):
        company = request.session['company-id']
        company_logo = FilmCompany.objects.filter(id=company)
        context = {'details':company_logo}
        if request.method == 'POST':
            company_details = FilmCompany.objects.get(id=company)
            logo = request.FILES['image']
            company_details.company_log = logo
            company_details.save()
            return render(request,'company/profile.html',context)
        else:
            return render(request,'company/profile.html',context)
    else:
        return render(request,'company/login.html')

def userimage_upload(request):
    if request.session.has_key('user-id'):
        userid = request.session['user-id']
        user = UserRegister.objects.filter(id=userid)
        context = {'edit':user}
        if request.method == 'POST':
            user_details = UserRegister.objects.get(id=userid)
            image = request.FILES['image']
            user_details.profile_image = image
            user_details.save()
            return render(request,'user/profile.html',context)
        else:
            return render(request,'user/profile.html',context)
    else:
        return render(request,'user/login.html')

def company_logout(request):
    if request.session.has_key('company-id'):
        del request.session['company-id']
        return redirect('home')
    else:
        return render(request,'company/login.html')

def user_logout(request):
    if request.session.has_key('user-id'):
        del request.session['user-id']
        return redirect('home')
    else:
        return render(request,'user/login.html')

def company_login(request):
    if request.session.has_key('company-id'):
        return redirect('/companyhome/')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['pass']
            company_details = FilmCompany.objects.all().filter(email=email,password=password,status='approve')
            for i in company_details:
                request.session['company-id']=i.id
                companyid = i.id
            if company_details:
                details = FilmCompany.objects.filter(id=companyid)
                context = {'details':details}
                return render(request,'company/companyhome.html',context)
            else:
                message = 'Invaild email and password!'
                return render(request,'company/login.html',{'message':message})
        else:
            return render(request,'company/login.html')

def company_register(request):
    if request.session.has_key('company-id'):
        return redirect('/companyhome/')
    else:
        if request.method == 'POST':
            logo = request.FILES.get('logo')
            companyname = request.POST['companyname']
            email = request.POST['email']
            password = request.POST['pass']
            phone = request.POST['phonenumber']
            company_details = FilmCompany(company_log=logo,company_name=companyname,email=email,password=password,phone_number=phone,status='pending')
            company_details.save()
            return render(request,'company/login.html')
        else:
            return render(request,'company/register.html')

def castcall_register(request):
    if request.session.has_key('company-id'):
        companyid = request.session['company-id']
        tags= Tags.objects.all()
        context = {'tags':tags}
        if request.method == 'POST':
            title = request.POST['title']
            image = request.FILES['image']
            role = request.POST['role']
            roledescription = request.POST['rol_des']
            location = request.POST['location']
            gender = request.POST['gender']
            productiondescription = request.POST['pro_des']
            age = request.POST['age']
            expire = request.POST['expire']
            tags = request.POST.getlist('tags')
            company = FilmCompany.objects.get(id=companyid)
            castcall_details = CastRegister(castcall_image=image,company_id=company,title=title,production_description=productiondescription,gender=gender,expire=expire,audition_location=location,age=age,role=role,role_description=roledescription,status='pending')
            castcall_details.save()
            for item in tags:
                castcall_details.tags.add(item)
            return render(request,'company/castcallregisterpage.html',context)
        else:
            return render(request,'company/castcallregisterpage.html',context)
    else:
        return render(request,'company/login.html')

def film_tags(request):
    if request.session.has_key('company-id'):
        if request.method == 'POST':
            tag = request.POST['tag']
            tag_name = Tags(category=tag)
            tag_name.save()
            return render(request,'company/filmtags.html')
        else:
            return render(request,'company/filmtags.html')

def film_promotion(request):
    if request.session.has_key('company-id'):
        company = request.session['company-id']
        total_tags = Tags.objects.all()
        context = {'tags':total_tags}
        if request.method == 'POST':
            company_id = FilmCompany.objects.get(id=company)
            pro_video = request.FILES['pro_video']
            tags = request.POST.getlist('tags')
            promotion_details = FilmPromotion(company_id=company_id,promotion_video=pro_video)
            promotion_details.save()
            for tag in tags:
                promotion_details.category.add(tag)
            return render(request,'company/filmpromotion.html',context)
        else:
            return render(request,'company/filmpromotion.html',context)

    else:
        return render(request,'company/login.html')

def castcall_view(request):
    if request.session.has_key('user-id'):
        castcall_id = request.GET['id']
        clickedcastcall_details= CastRegister.objects.filter(id=castcall_id)
        context = {'details':clickedcastcall_details}
        return render(request,'user/castcallviewpage.html',context)
    else:
        return render(request,'user/login.html',{'error':'login please'})

def castcall_apply(request):
    if request.session.has_key('user-id'):
        user = request.session['user-id']
        clickedcastcall_id = request.GET['id']
        castcall_id = CastRegister.objects.get(id=clickedcastcall_id)
        user_id = UserRegister.objects.get(id=user)
        castcall_booking = CastBooking(cast_id=castcall_id,user_id=user_id,approve_status='pending')
        castcall_booking.save()
        return redirect('/userhome/')


def adminuser_view(request):
    if request.session.has_key('admin-id'):
        user_details = UserRegister.objects.all().filter(status='pending')
        user_id = request.GET.get('id')
        UserRegister.objects.all().filter(id=user_id).update(status='approve')
        context = {'user_request':user_details,'user_header':'0'}
        return render(request,'admin/user.html',context)
    else:
        return redirect('/admin/')

def admincompany_view(request):
    if request.session.has_key('admin-id'):
        company_details = FilmCompany.objects.all().filter(status='pending')
        company_id = request.GET.get('id')
        FilmCompany.objects.all().filter(id=company_id).update(status='approve')
        context = {'company_request':company_details,'company_header':"0"}
        return render(request,'admin/company.html',context)
    else:
        return redirect('/admin/')

def admincast_view(request):
    if request.session.has_key('admin-id'):
        totalcastcall_details = CastRegister.objects.all().filter(status='pending')
        clickedcastcall_id = request.GET.get('id')
        CastRegister.objects.all().filter(id=clickedcastcall_id).update(status='approve')
        context={'cast_details':totalcastcall_details}
        return render(request,'admin/cast.html',context)
    else:
        return redirect('/admin/')

def usercastcallrequest_approve(request):
    if request.session.has_key('company-id'):
        applied_castcall_id = request.GET.get('id')
        CastBooking.objects.all().filter(id=applied_castcall_id).update(approve_status='approved')
        total_applied_castcalls = CastBooking.objects.all().filter(approve_status='pending')
        context = {'total_castcall':total_applied_castcalls}
        return render(request,'company/usercastcall.html',context)
    else:
        return redirect('/companylogin/')

def admintotaluser_view(request):
    user_details = UserRegister.objects.all().filter(status='approve')
    context = {'user_total':user_details,'user_header':'0'}
    return render(request,'admin/user.html',context)

def admintotalcompany_view(request):
    company_details = FilmCompany.objects.all().filter(status='approve')
    context = {'company_total':company_details,'company_header':'0'}
    return render(request,'admin/company.html',context)


def promotion_video(request):
    video_details = FilmPromotion.objects.all()
    context = {'video':video_details}
    return render(request,'user/promotionvideo.html',context)

def usertotalcast_call(request):
    user = request.session['user-id']
    applied_castcall = CastBooking.objects.all().filter(user_id=user)
    context = {'castcall':applied_castcall}
    return render(request,'user/totalcastcall_applied.html',context)

def castcall_delete(request):
    castcall_id = request.GET.get('id')
    CastBooking.objects.all().filter(id=castcall_id).delete()
    return redirect('/usertotalcastcall/')
