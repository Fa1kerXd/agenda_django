from django.shortcuts import render
from contact.forms import RegisterUser, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


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

@login_required(login_url="contact:login")
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)


    if not request.method is 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
             'form': form,   
            }
        )
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
             'form': form,   
            }
        )
    form.save()
    auth.login(request, request.user)
    return redirect('contact:user_update')




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

@login_required(login_url="contact:login")
def logout_view(request):
    auth.logout(request)
    messages.info(request, "Você fez logout com sucesso!")
    return redirect('contact:login')