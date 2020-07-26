from django.shortcuts import render,redirect
from Main.models import *

def home(request):
    return render(request,'base/home.html')

def user_home(request):
    return render(request,'user/homepage.html')

def company_home(request):

    return render(request,'company/companyhome.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user_details = UserRegister.objects.all().filter(username=username,password=password)
        for i in user_details:
            request.session['user-id']=i.id
        if user_details:
            return render(request,'user/homepage.html')
        else:
            message = 'Invaild username and password!'
            return render(request,'user/login.html',{'message':message})
    else:
        return render(request,'user/login.html')

def user_register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        phonenumber = request.POST['phoneno']
        password = request.POST['pass']
        user_details = UserRegister(profile_image='user/default.jpg',fullname=fullname,username=username,email=email,password=password,phone_number=phonenumber,status='pending')
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

def userimage_upload(request):
    if request.session.has_key('user-id'):
        userid = request.session['user-id']
        user_details = UserRegister.objects.filter(id=userid)
        context = {'edit':user_details}
        if request.method == 'POST':
            image = request.FILES['image']
            user_details.profile_image = image
            user_details.save()
            return render(request,'user/profile.html',context)
        else:
            return render(request,'user/profile.html',context)
    else:
        return render(request,'user/login.html')


def user_logout(request):
    if request.session.has_key('user-id'):
        del request.session['user-id']
        return redirect('home')
    else:
        return render(request,'user/login.html')

def company_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        company_details = FilmCompany.objects.all().filter(email=email,password=password)
        for i in company_details:
            request.session['company-id']=i.id
        if company_details:
            return render(request,'company/companyhome.html')
        else:
            message = 'Invaild email and password!'
            return render(request,'company/login.html',{'message':message})
    else:
        return render(request,'company/login.html')

def company_register(request):
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
        tags = Tags.objects.all()
        context = {'tags':tags}
        if request.method == 'POST':
            company_id = FilmCompany.objects.get(id=company)
            pro_video = request.FILES['pro_video']
            tag = request.POST.getlist('tags')
            promotion_details = FilmPromotion(company_id=company_id,promotion_video=pro_video)
            promotion_details.save()
            for tag in tag:
                promotion_details.category.add(tag)
            return render(request,'company/filmpromotion.html',context)
        else:
            return render(request,'company/filmpromotion.html',context)

    else:
        return render(request,'comapny/login.html')
