

from django.db import models


from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Skill(models.Model):
    name = models.CharField(max_length=20,blank=True, null= True)
    score = models.IntegerField(default=80,blank=True,null=True) 
    image = models.FileField(blank=True, null=True,upload_to="skills")
    is_key_skill = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    class Meta:     
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"

   

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(blank = True, null = True, upload_to='avatar')
    title = models.CharField(max_length=200,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    skills = models.ManyToManyField(Skill,blank=True)
    cv = models.FileField(blank=True,null=True,upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f' {self.name}'



class Testimonals(models.Model):

    thumbnail = models.ImageField(blank = True, null = True, upload_to='thumbnail')
    name = models.CharField(max_length=200,blank=True,null=True)
    role = models.CharField(max_length=200,blank=True,null=True)
    quota = models.CharField(max_length=200,blank=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Media(models.Model):
     image = models.ImageField(blank = True, null = True, upload_to='media')
     is_image = models.BooleanField(default=True)
     name = models.CharField(max_length=200,blank=True,null=True)
     url = models.URLField(blank=True,null=True)


     def save(self,*args,**kargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args,**kargs)

class Portfolio(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    body = RichTextField(blank=True,null=True)
    date = models.DateTimeField(blank=True,null=True)
    image = models.ImageField(blank = True, null = True, upload_to='portfolio')
    slug = models.SlugField(blank=True,null=True)


    def save(self,*args,**kargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args,**kargs)   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'

class Blog(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    body = RichTextField(blank=True,null=True)
    date = models.DateTimeField(blank=True,null=True)
    image = models.ImageField(blank = True, null = True, upload_to='portfolio')
    slug = models.SlugField(blank=True,null=True)


    def save(self,*args,**kargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args,**kargs)   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/Blog/{self.slug}'


class Certificate(models.Model):
    date = models.DateTimeField(blank=True,null=True)
    name = models.CharField(max_length=50,blank=True,null=True)

    title =models.CharField(max_length=200,blank=True,null=True)
    description = models.CharField(max_length=200,blank=True,null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name




    



