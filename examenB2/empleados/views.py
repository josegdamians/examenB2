from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AgregarEmpleado
from .models import Empleado
from .models import Empresa
from .models import Departamento


def index(request):
    queryset = request.GET.get("criterio")
    queryempresa = request.GET.get("empresa")
    querydepartamento = request.GET.get("departamento")
    empleados = Empleado.objects.all()
    empresas = Empresa.objects.all()
    departamentos = Departamento.objects.all()

    if queryset:
        empleados = Empleado.objects.filter(nombre__contains=queryset)

    if queryempresa:
        empleados = Empleado.objects.filter(empresa=Empresa.objects.get(id__iexact = queryempresa))
    
    if querydepartamento:
        empleados = Empleado.objects.filter(departamento=Departamento.objects.get(id__iexact = querydepartamento))

    context = {'empleados':empleados,'empresas':empresas,'departamentos':departamentos}
    return render(request, 'empleados/index.html', context)


def add(request):
    if request.method == "POST":
        form = AgregarEmpleado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AgregarEmpleado()
    context = {'form' : form}
    return render(request, "empleados/add.html", context)


def delete(request, empleado_id):
    empleado = Empleado.objects.get(id = empleado_id)
    empleado.delete()
    return redirect("index")


def edit(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    if request.method == "POST":
        form = AgregarEmpleado(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AgregarEmpleado(instance=empleado)
    
    context = {"form" : form}
    return render(request, "empleados/edit.html", context)

