from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def accueil(request):
    return render(request, "accueil.html")
