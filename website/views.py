from django.shortcuts import render
from website.models import Pessoa

# Create your views here.

def index(request):
    contexto = {}
    if request.method == 'post' :
        Pessoa = Pessoa()
        Pessoa.nome = request.post['nome']




    return render(request, 'index.html', contexto)


def sobre(request):
    Pessoa =Pessoa
    contexto = {

        
    }
    return render(request, 'sobre.html', contexto)
#python manage.py makemigrations = gera arquivo de migração 
#python manage.py  migrate = através do arquivo gerado ele cria ou modifica a base de dados 