from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def guojin(request):

    return render(request,'guojin/guojin.html')
