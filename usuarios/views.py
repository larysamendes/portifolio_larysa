from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from Jogos.models import Jogo
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco!')
            return redirect('cadastro')

        if not email.strip():
            print('O campo email não pode ficar em branco!')
            return redirect('cadastro')

        if not senha1.strip():
            print('O campo senha não pode ficar em branco!')
            return redirect('cadastro')

        if senha1 != senha2:
            print('')
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')

        if User.objects.filter(email = email).exists():
            print('Usuario já cadastrado!')
            return redirect('cadastro')

        if User.objects.filter(username = nome).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')

        usuario = User.objects.create_user(username=nome, email=email, password=senha1)
        usuario.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if senha.strip() == "":
            messages.error(request, 'O campo senha não pode ficar em branco!')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')
            else:
                print('')
                messages.error(request, 'O email ou senha estão incorretos!')
        else:
            print('')
            messages.error(request, 'O email ou senha estão incorretos!')
    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        jogos = Jogo.objects.filter(usuario=id)
        dados = {
            'jogos': jogos
        }

        return render(request, 'usuarios/dashboard.html',dados)
    else:
        return redirect('index')

