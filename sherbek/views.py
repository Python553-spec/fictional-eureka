from django.shortcuts import render
from django.http import HttpResponse
# def Bugalterya(request):
#     html = """
#     <h1>Bug'alteya</h1>
# """
    # return HttpResponse(html)



def index(request):
    return render(request,'index.html')