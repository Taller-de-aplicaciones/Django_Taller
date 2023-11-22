from django.shortcuts import render, redirect, get_object_or_404
from appWeb.models import Analista, Entrevistador
from appWeb.forms import AnalistaForm


# Create your views here.
def Inicio(request):
    return render(request, "appWebTemplates/inicio.html")

def Dashboard(request):
    return render(request,'appWebTemplates/dashboard.html')

def VerListas(request):
    return render(request,'appWebTemplates/listasUsuarios.html')

def all_analistas(request):
    analistas = Analista.objects.all()
    
    data = {'analistas': analistas}

    return render(request,'appWebTemplates/menuAnalistas.html', data)

def crear_analista(request):
    if request.method == 'POST':
        form = AnalistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaAnalistas')
    else:
        form = AnalistaForm()
    return render(request, 'appWebTemplates/analistaAdd.html',{'form':form})

def cargar_detalles_analista(request,analista_id):
    analista = get_object_or_404(Analista, id=analista_id)
    form = AnalistaForm(instance=analista)

def editar_analista(request, analista_id):
    analista = get_object_or_404(Analista, id=analista_id)

    if request.method == 'POST':
        form = AnalistaForm(request.POST, instance=analista)
        if form.is_valid():
            form.save()
            return redirect('listaAnalistas')
    else:
        form = AnalistaForm(instance=analista)
    return render(request,'appWebTemplates/analistaEdit.html',{'form':form})

def eliminar_analista(request, analista_id):
    analista = get_object_or_404(Analista, id=analista_id)

    if request.method == 'POST':
        analista.delete()
        return redirect('listaAnalistas')
    return render(request,'appWebTemplates/analistaDel.html',{'analista':analista})

def all_entrevistadores(request):
    entrevistadores = Entrevistador.objects.all()
    
    data = {'entrevistadores': entrevistadores}

    return render(request,'appWebTemplates/menuEntrevistadores.html', data)

def crear_entrevistador(request):
    if request.method == 'POST':
        form = EntrevistadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaEntrevistadores')
    else:
        form = EntrevistadorForm()
    return render(request, 'appWebTemplates/entrevistadorAdd.html',{'form':form})

def editar_entrevistador(request, entrevistador_id):
    entrevistador = get_object_or_404(Entrevistador, id=entrevistador_id)

    if request.method == 'POST':
        form = EntrevistadorForm(request.POST, instance=entrevistador)
        if form.is_valid():
            form.save()
            return redirect('listaEntrevistadores')
    else:
        form = EntrevistadorForm(instance=entrevistador)
    return render(request,'appWebTemplates/entrevistadorEdit.html',{'form':form})

def eliminar_entrevistador(request, entrevistador_id):
    entrevistador = get_object_or_404(Entrevistador, id=entrevistador_id)

    if request.method == 'POST':
        Entrevistador.delete()
        return redirect('listaEntrevistadores')
    return render(request,'appWebTemplates/entrevistadorDel.html',{'entrevistador':entrevistador})