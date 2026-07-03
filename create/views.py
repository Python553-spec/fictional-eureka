from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import sherbek212

def index2(request):
    if request.method == "POST":
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        sherbek212.objects.create(
            name=name,
            last_name=last_name)
        return redirect("/")
    
    return render(request, "indexa.html")