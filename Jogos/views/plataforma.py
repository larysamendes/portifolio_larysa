from django.shortcuts import render, get_object_or_404, redirect
from Jogos.models import Plataforma

def cria_plataforma(request):
    if request.method == 'POST':

        nomes = request.POST['nomePla']
        if not nomes.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('criar_plataforma')

        plataforma = Plataforma.objects.create(nomePla=nomes)
        plataforma.save()

        return redirect('dashboard')

    else:
        return render(request, 'plataformas/cria_plataforma.html')