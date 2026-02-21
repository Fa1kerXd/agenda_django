from django.shortcuts import render
from contact.forms import RegisterUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect



def register(request):
    form = RegisterUser()

    if request.method == 'POST':
        form = RegisterUser(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Conta Criada com Sucesso!")
            return redirect('contact:login')
            
    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )


def login_form(request):
    form =  AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request,user)
            messages.success(request,"User Autenticado com sucesso!")
            return redirect('contact:index')

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
            'title': '',
        }
        )


def logout_view(request):
    auth.logout(request)
    messages.info(request, "Você fez logout com sucesso!")
    return redirect('contact:login')