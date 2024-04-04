from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def listar_receitas(request):
    nome = 'Gabriel'
    ingredientes = ['Farinha', 'Ovo', 'Manteiga', 'Leite']

    #dicionario que vai levar os dados para o template
    #chave : valor
    context = {
        'Endereco' : 'Av Marechal Tito',
        'Bairro' : 'São Miguel Paulista',
        'Cidade' : 'São Paulo',
        'Estado' : 'SP',
        'Nome' : nome,
        'Ingredientes' : ingredientes
    }



    #Qual template essa view vai retornar
    return render(request, 'receitas.html', context)