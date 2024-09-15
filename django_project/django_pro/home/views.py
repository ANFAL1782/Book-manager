from django.shortcuts import render
from django.http import HttpResponse
from .Forms import RegistorForm
from. models import Teachers,Books

# Create your views here.
def Index(request):
    return render(request,'index.html')
def About(request):
    return render(request,'About.html')
def TeachersPage(request):
    dict_teach={
        'teach': Teachers.objects.all()
    }
    return render(request,'Teachers.html',dict_teach)

def Registor(request):
    if request.method =="POST":
        form = RegistorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=RegistorForm()
    dict_form={
        'form':form
    }
    return render(request,'Registor.html',dict_form)

def Bookpage(request):
    dict_Book={
        'Book': Books.objects.all()
    }
    
    return render(request,'Book.html', dict_Book)
def Contact(request):
    return render(request,'Contact.html')


