from django.shortcuts import render
from .models import Personal
from django.views.generic.list import ListView
# Create your views here.
from django.http import HttpResponse

from .models import Menu


def menu(request):
    menu=Menu.objects.all()
    pic=[]
    for item in menu:
        pic.append(item.picture)

    return render(request,'menu.html', {'menu':menu,'pic':pic})


def main(request):
    person=[]
    for item in Personal.objects.all():
        person.append(f"{item.fio} '-' {item.job_adress}")
    context= {
        'title':'Ресторан национальной кухни',
        "person": person, }
    return render(request, "main.html",context)


def about(request):
    return render(request,'about.html')

def register(request):
    return render(request,'register.html')


def delivery(request):
    return render(request,'delivery.html')

# def main(request):
#     person=[]
#     for item in Personal.objects.all():
#         person.append(f"{item.fio} '-' {item.job_adress}")
#     context= {"person": person, }
#     return render(request, "main.html",context)
