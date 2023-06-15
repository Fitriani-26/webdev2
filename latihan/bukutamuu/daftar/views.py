from django.shortcuts import render
from django.http import HttpResponse
from daftar.models import pdaftar

def Home(req):
    return render(req,"home.html")

def Daftar(req):
    registrasi = pdaftar.objects.all ()
    return render(req,"daftar.html",{"registrasi":registrasi}) 

def Contact(req):
    return render(req,"kontak.html")
