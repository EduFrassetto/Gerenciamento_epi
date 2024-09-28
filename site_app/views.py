from django.shortcuts import render, redirect
from site_app.models import Colaborador
from site_app.models import Epi
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

def cadastro_epi(request):
    nome_epi = None
    if request.method == 'POST':
        nome_epi = request.POST.get('nome_epi')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        lote = request.POST.get('lote')
        validade = request.POST.get('validade')
        validade_uso = request.POST.get('validade_uso')
        status = request.POST.get('status')
        if nome_epi:
            Epi.objects.create(
                nome_epi=nome_epi,
                marca=marca,
                modelo=modelo,
                lote=lote,
                validade=validade,
                validade_uso=validade_uso,
                status=status
            )
        print(nome_epi, marca, modelo, lote, validade, validade_uso, status)
    return render(request, 'site_app/global/cadastro_epi.html', {'ultimo_epi':nome_epi})

def lista_epi(request):
    values = Epi.objects.all()
    nome_epi = request.GET.get('nome_epi')
    if nome_epi:
        values = Epi.objects.filter(nome_epi__icontains=nome_epi)
    return render(request, 'site_app/global/lista_epi.html', {"lista_epi":values})
