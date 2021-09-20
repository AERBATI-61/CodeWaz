from django.db import models

# Create your models here.
class Category(models.Model):
    title       = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Project(models.Model):
    url         = models.TextField()
    title       = models.CharField(max_length=128)
    image       = models.ImageField(upload_to='project/')
    category    = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    date        = models.DateField(auto_now_add=True)
    author      = models.CharField(max_length=128)
    description = models.TextField()



    def __str__(self):
        return self.title


class Service(models.Model):
    title       = models.CharField(max_length=128)
    image       = models.ImageField(upload_to='service/')
    description = models.TextField()

    def __str__(self):
        return self.title



class Slider(models.Model):
    title      = models.CharField(max_length=128)
    title1       = models.CharField(max_length=128)
    title2       = models.CharField(max_length=128)
    title3       = models.CharField(max_length=128)
    title4       = models.CharField(max_length=128)
    image        = models.ImageField(upload_to='slider/')
    description  = models.TextField()

    def __str__(self):
        return self.title




class Rise(models.Model):
    title       = models.CharField(max_length=128)
    subtitle    = models.TextField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class RiseJob(models.Model):
    title       = models.CharField(max_length=128)
    subtitle    = models.TextField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



class Contact(models.Model):
    name                = models.CharField(max_length=64)
    phone_number        = models.CharField(max_length=16,null=True,blank=True)
    email               = models.EmailField(null=True,blank=True)
    subject             = models.CharField(max_length=256)
    description         = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.name


class OurDetail(models.Model):
    name                = models.CharField(max_length=64)
    title = models.CharField(max_length=256)
    phone_number        = models.CharField(max_length=16,null=True,blank=True)
    email               = models.EmailField(null=True,blank=True)
    description         = models.TextField(null=True,blank=True)
    image               = models.ImageField(upload_to='ourdetail/')


    def __str__(self):
        return self.name