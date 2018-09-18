from django.db import models

class Onlineregister(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name="ID")
    firstName = models.CharField(max_length=100, verbose_name="First Name")
    lastName = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(max_length=100, verbose_name="Email id")
    zipcode = models.IntegerField(max_length=None, verbose_name="Zipcode")
    sex = models.CharField(max_length=10, verbose_name="Sex")
    birth = models.DateField(verbose_name="Date of Birth")
    password = models.CharField(max_length=100, verbose_name="Password")

    def _str_(self):
        form = PostForm()
        return self.firstname
    class Meta:
        #model = Post
        db_table = ('onlineregister')
        app_label = ('sampledata')

    

class Login(models.Model):
    user_id = models.IntegerField(primary_key=True, verbose_name="User_id")
    email_id = models.EmailField(max_length=100, verbose_name="Email id")
    password = models.CharField(max_length=100, verbose_name="Password")

    def _str_(self):
        form = PostForm()
        return self.user_id

    class Meta:
       # model = Post
        db_table = ('login')
        app_label = ('sampledata')

        

