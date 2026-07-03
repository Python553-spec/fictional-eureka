from django.shortcuts import render,redirect
from django.http import HttpResponse
# def bola(requests):
#     return render(requests,'bola.html')
from .models import bola
# def bola_list(requests):
#     bolalar = bola.objects.all()
#     return render(requests,'bola.html',{'bolalar':bolalar})
def index2(reqests):
    if reqests.method == "POST":
        name = reqests.POST.get("name")
        narxi = reqests.POST.get("narxi")
        malumot  = reqests.POST.get("malumot")
        rasm_yuklash = reqests.FILES.get("rasm")
        bola.objects.create(
            name=name,
            narxi=narxi,
            malumot=malumot,
            rasm=rasm_yuklash
        )
        return redirect('/bola/sherbek/')
    return render(reqests,"bola.html")

def sherbek_view(request):
    bolalar_list = bola.objects.all()
    return render(request, "sherbek.html", {"bolalar": bolalar_list})


def bola_delete(request, id):
    bola.objects.filter(id=id).delete()
    return redirect('/bola/sherbek/')