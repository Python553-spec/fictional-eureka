from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
# def test(request):
#     html = """
#     <h1>Hello World</h1>
# """
#     return HttpResponse(html)

def test(request):
    if request.method == "POST":
        User.objects.create(
            name = request.POST.get("ism"),
            familya = request.POST.get("familya"),
            age = request.POST.get("age"),
        )

        return redirect("index")
    return render(request, "index.html")
