from django.shortcuts import render, redirect
from site_app.models import Colaborador
data = [
    {'nome':'Eduardo'}
]
# Create your views here.
def home(request):
    return render(request, 'site_app/global/home.html')

def cadastro_colaborador(request):
    nome = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        cargo = request.POST.get('cargo')
        status = request.POST.get('status')
        if nome:
            Colaborador.objects.create(
                nome=nome,
                data_nascimento=data_nascimento,
                cpf=cpf,
                telefone=telefone,
                cargo=cargo,
                status=status
            )
        print(nome, data_nascimento, cpf, telefone, cargo, status)
    return render(request, 'site_app/global/cadastro_colaborador.html', {'ultimo_cadastro':nome})

def lista_colaborador(request):
    values = Colaborador.objects.all()
    nome = request.GET.get('nome')
    if nome:
        values = Colaborador.objects.filter(nome__icontains=nome)
    
    return render(request, 'site_app/global/lista_colaborador.html', {"lista_colaborador":values})

def deletar_colaborador(request, id):
    colaborador = Colaborador.objects.get(id=id)
    colaborador.delete()
    return redirect('lista_colaborador')

def atualizar_colaborador(request, id):
    colaborador = Colaborador.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        cargo = request.POST.get('cargo')
        status = request.POST.get('status')
        if nome and data_nascimento and cpf and telefone and cargo and status:
            colaborador.nome = nome
            colaborador.data_nascimento = data_nascimento
            colaborador.cpf = cpf
            colaborador.telefone = telefone
            colaborador.cargo = cargo
            colaborador.status = status
            colaborador.save()
            return redirect('lista_colaborador')
        else:
            return render(request, 'site_app/global/atualizar_colaborador.html', {"colaborador":colaborador, "erro":True})
    return render(request, 'site_app/global/atualizar_colaborador.html', {"colaborador":colaborador})