from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Student3(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    file = models.FileField(upload_to="files/")


class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_address= models.CharField(max_length=100)

class Student2(models.Model):
    gender_choices = (("Male","Male"),("Female","Female"))
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()
    gender = models.CharField(max_length=10,choices=gender_choices,default="Male")
    age = models.IntegerField(null=True,blank=True)
    student_bio = models.TextField()