from django.shortcuts import render, get_object_or_404 , redirect
from Jogos.models import Genero

def cria_genero(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('criar_plataforma')

        genero = Genero.objects.create(tipo=nome)
        genero.save()

        return redirect('dashboard')

    else:
        return render(request, 'generos/cria_genero.html')
