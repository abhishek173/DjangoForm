from django.shortcuts import render,redirect
from home.forms import StudentForm
from .models import Student3
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        file = request.FILES['file']

        Student3.objects.create(name=name,age=age,gender=gender,file=file)
        return redirect('/thank-you/')

    context = {
        'form':StudentForm
    }
    return render(request,"index.html",context)

def thankyou(request):
    return HttpResponse("<h1>Student Registered Successfully..</h1>")