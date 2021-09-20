from django.shortcuts import render, get_object_or_404, redirect
from Jogos.models import  Desenvolvedor

def cria_desenvolvedor(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('criar_plataforma')
        cidade = request.POST['cidade']
        if not cidade.strip():
            print('O campo cidade não pode ficar em branco')
            return redirect('criar_plataforma')
        estado = request.POST['estado']
        if not estado.strip():
            print('O campo estado não pode ficar em branco')
            return redirect('criar_plataforma')
        pais = request.POST['pais']
        if not pais.strip():
            print('O campo pais não pode ficar em branco')
            return redirect('criar_plataforma')

        desenvolvedor = Desenvolvedor.objects.create(nome=nome, cidade=cidade, estado= estado, pais=pais)
        desenvolvedor.save()

        return redirect('dashboard')

    else:

        return render(request, 'desenvolvedores/cria_desenvolvedor.html')