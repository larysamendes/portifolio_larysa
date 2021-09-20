
from django.shortcuts import render, get_object_or_404, redirect
from Jogos.models import Jogo, Genero, Plataforma , Desenvolvedor
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    jogos = Jogo.objects.filter(publicar=True)
    dados = {
        'jogos' : jogos
    }
    return render(request,'index.html', dados)


def jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    jogo_a_exibir = {
        'jogo' : jogo
    }
    return render(request,'jogo.html', jogo_a_exibir)


def buscar(request):
    lista_jogos = Jogo.objects.filter(publicar=True)

    if 'buscar' in request.GET:

        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_jogos = lista_jogos.filter(nome__icontains=nome_a_buscar)

    dados = {
        'jogos': lista_jogos
    }

    return render(request, 'buscar.html', dados)


def cria_jogo(request):
    genero = Genero.objects.all()
    plataforma = Plataforma.objects.all()
    desenvolvedor = Desenvolvedor.objects.all()

    dados = {
        'generos': genero,
        'plataformas': plataforma,
        'desenvolvedores': desenvolvedor,
    }

    if request.method == 'POST':
        usuario = get_object_or_404(User, pk=request.user.id)
        nome = request.POST['nome']
        data = request.POST['ano_pub']

        genero_id = request.POST.getlist('genero')
        lista_generos = []
        for id in genero_id:
            genero = get_object_or_404(Genero, pk=id)
            lista_generos.append(genero)

        plataforma_id = request.POST.getlist('plataforma')
        lista_plataformas = []
        for id in plataforma_id:
            plataforma = get_object_or_404(Plataforma, pk=id)
            lista_plataformas.append(plataforma)

        enredo = request.POST['enredo']
        critica = request.POST['critica']
        avaliacao = request.POST["nota"]

        desenvolvedor_id = request.POST.getlist("desenvolvedor")
        lista_desenvolvedores = []
        for id in desenvolvedor_id:
            desenvolvedores = get_object_or_404(Desenvolvedor, pk=id)
            lista_desenvolvedores.append(desenvolvedores)

        capa_jogo = request.FILES["capa_jogo"]

        jogo = Jogo.objects.create(usuario=usuario, nome=nome, data=data,
                                   enredo=enredo,critica=critica, avaliacao=avaliacao, capa_jogo=capa_jogo)
        jogo.genero.set(lista_generos)
        jogo.desenvolvedores.set(lista_desenvolvedores)
        jogo.plataforma.set(lista_plataformas)
        jogo.save()
        messages.success(request, 'Jogo cadastrado com sucesso!')
        return redirect('dashboard')

    return render(request, 'jogos/cria_jogos.html', dados)

def deleta_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    jogo.delete()
    messages.success(request, 'Jogo deletado com sucesso!')
    return redirect('dashboard')


def edita_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    genero = Genero.objects.all()
    plataforma = Plataforma.objects.all()
    desenvolvedor = Desenvolvedor.objects.all()

    dados = {
        'generos': genero,
        'plataformas': plataforma,
        'desenvolvedores': desenvolvedor,
        'jogo': jogo,
    }

    return render(request, 'jogos/edita_jogos.html', dados)

def atualiza_jogo(request):
    if request.method == 'POST':
        jogo_id = request.POST['jogo_id']
        j = get_object_or_404(Jogo, pk=jogo_id)
        j.nome = request.POST['nome']
        j.data = request.POST['ano_pub']

        genero_id = request.POST.getlist('genero')
        lista_generos = []
        for id in genero_id:
            generos = get_object_or_404(Genero, pk=id)
            lista_generos.append(generos)

        plataforma_id = request.POST.getlist('plataforma')
        lista_plataformas = []
        for id in plataforma_id:
            plataformas = get_object_or_404(Plataforma, pk=id)
            lista_plataformas.append(plataformas)
        j.plataforma.set(lista_plataformas)

        j.enredo = request.POST['enredo']
        j.critica = request.POST['critica']
        j.avaliacao = request.POST["nota"]

        desenvolvedor_id = request.POST.getlist("desenvolvedor")
        lista_desenvolvedores = []
        for id in desenvolvedor_id:
            desenvolvedores = get_object_or_404(Desenvolvedor, pk=id)
            lista_desenvolvedores.append(desenvolvedores)

        j.plataforma.set(lista_plataformas)
        j.desenvolvedores.set(lista_desenvolvedores)
        j.genero.set(lista_generos)

        if 'capa_jogo' in request.FILES:
            j.capa_jogo = request.FILES["capa_jogo"]

        j.save()
        messages.success(request, 'Jogo atualizado com sucesso!')
        return redirect('dashboard')