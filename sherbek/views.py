from django.shortcuts import render, redirect
from .models import Ishchi

# def index(request):
#     if request.method == 'POST':
#         # Formadan ma'lumotlarni olish
#         Conter.objects.create(
#             ismi=request.POST.get('ismi'),
#             familya=request.POST.get('familya'),
#             raqam=request.POST.get('raqam'),
#             yoshi=request.POST.get('yoshi'),
#             stem_username=request.POST.get('stem_username'),
#             telegram_username=request.POST.get('telegram_username')
#         )
#         # Ma'lumot saqlangandan so'ng ikkinchi sahifaga o'tkazish
#         return redirect('index1')
    
#     return render(request, 'index.html')

# def index1(request):
#     # Bu ikkinchi sahifani ko'rsatadi
#     return render(request, 'index1.html')

# def users_list(request):
#     users = Sherbek.objects.all()
#     return render(request, 'users_list.html',{'users':users})


# views.py ichida






























# from django.shortcuts import render, redirect
# from .models import Sherbek

# def index2(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         surname = request.POST.get('surname')
#         Sherbek.objects.create(name=name, surname=surname)
#         return redirect('index')
    
#     return render(request, 'index.html')












def create_ishchi(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')

        Ishchi.objects.create(
            name=name,
            surname=surname,
        )

        return redirect('/ishchilar')

    return render(request, 'ishchi_form.html')


def ishchilar(request):
    ishchilar = Ishchi.objects.all()
    return render(request, 'ishchilar.html', {'ishchilar': ishchilar})



def update_ishchi(request, id):
    ishchi = Ishchi.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')

        ishchi.name = name
        ishchi.surname = surname

        ishchi.save()

        return redirect('/ishchilar')

    return render(request, 'ishchi_form.html', {'ishchi': ishchi})


    

def delete_ishchi(request, id):
    ishchi = Ishchi.objects.get(id=id)
    ishchi.delete()
    return redirect('/ishchilar')


def index2(request):
    return render(request, 'index2.html')









# def register(request):
#     return render(request, 'index.html') # index.html sahifasini ochadi
# from django.shortcuts import render, redirect
# from .models import Conter

# def index(request):
#     if request.method == 'POST':
#         # Formadan ma'lumotlarni olish
#         Conter.objects.create(
#             ismi=request.POST.get('ismi'),
#             familya=request.POST.get('familya'),
#             raqam=request.POST.get('raqam'),
#             yoshi=request.POST.get('yoshi'),
#             stem_username=request.POST.get('stem_username'),
#             telegram_username=request.POST.get('telegram_username')
#         )
#         return redirect('index1')
    
#     return render(request, 'index.html')

# def index1(request):
#     return render(request, 'index1.html')



# from django.shortcuts import render, redirect
# from .forms import ConterForm

# def index(request):
#     if request.method == 'POST':
#         form = ConterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index1')
#     else:
#         form = ConterForm()
    
#     return render(request, 'index.html', {'form': form})



# from django.shortcuts import render, redirect
# from django.contrib.auth import logout
# from .forms import ConterForm

# def index(request):
#     if request.user.is_authenticated:
#         return redirect('success_page')

#     if request.method == 'POST':
#         form = ConterForm(request.POST)
#         if form.is_valid():
#             new_conter = form.save(commit=False)
            
#             if request.user.is_authenticated:
#                 new_conter.user = request.user
#             else:
#                 new_conter.user = None 
            
#             new_conter.save()
#             return redirect('success_page')
#     else:
#         form = ConterForm()
    
#     return render(request, 'index.html', {'form': form})

# def success_view(request):
#     return render(request, 'index1.html')


# from django.contrib.auth import logout
# from django.shortcuts import redirect

# def logout_view(request):
#     logout(request)
#     return redirect('index') 