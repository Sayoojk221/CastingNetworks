from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)

class UserRegister(models.Model):
    name = models.CharField(max_length=200,null=True)
    profile_image = models.ImageField(upload_to='user',null=True)
    email = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    district = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class FilmCompany(models.Model):
    company_name = models.CharField(max_length=200,null=True)
    company_log = models.ImageField(upload_to='company',null=True)
    email = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.company_name

class Tags(models.Model):
    category = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.category

class CastRegister(models.Model):
    company_id = models.ForeignKey(FilmCompany,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True)
    audition_date = models.CharField(max_length=200,null=True)
    audition_location = models.CharField(max_length=200,null=True)
    posted_time = models.TimeField(auto_now_add=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags)
    status = models.CharField(max_length=200,null=True)



class CastBooking(models.Model):
    cast_id = models.ForeignKey(CastRegister,on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    approve_status = models.CharField(max_length=200,null=True)

class FilmPromotion(models.Model):
    company_id = models.ForeignKey(FilmCompany,on_delete=models.CASCADE)
    promotion_image = models.ImageField(upload_to='promotion',null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200,null=True)
