from django.shortcuts import render, redirect
from restaurante.models import Plato

def platos_list(request):
    platos = Plato.objects.all()
    return render(request, "restaurante/platos/list.html", {"platos": platos})

def platos_create(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        plato = Plato(nombre=nombre, descripcion=descripcion, precio=precio)
        plato.save()
        return redirect("platos")
    return render(request, "restaurante/platos/form.html")

def platos_update(request, id):
    plato = Plato.objects.get(id=id)
    if request.method == "POST":
        plato.nombre = request.POST.get("nombre")
        plato.descripcion = request.POST.get("descripcion")
        plato.precio = request.POST.get("precio")
        plato.save()
        return redirect("platos")
    return render(request, "restaurante/platos/form.html", {"plato": plato})

def platos_delete(request, id):
    plato = Plato.objects.get(id=id)
    plato.delete()
    return redirect("platos")