from django.shortcuts import render, redirect
from restaurante.models import Cliente

def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, "restaurante/clientes/list.html", {"clientes": clientes})

def clientes_create(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        nit = request.POST.get("nit")
        cliente = Cliente(nombre=nombre, nit=nit)
        cliente.save()
        return redirect("clientes")
    return render(request, "restaurante/clientes/form.html")

def clientes_update(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        cliente.nombre = request.POST.get("nombre")
        cliente.nit = request.POST.get("nit")
        cliente.save()
        return redirect("clientes")
    return render(request, "restaurante/clientes/form.html", {"cliente": cliente})

def clientes_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("clientes")