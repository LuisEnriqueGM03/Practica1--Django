from django.shortcuts import render, redirect
from restaurante.models import Mesero

def meseros_list(request):
    meseros = Mesero.objects.all()
    return render(request, "restaurante/meseros/list.html", {"meseros": meseros})

def meseros_create(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        telefono = request.POST.get("telefono")
        mesero = Mesero(nombre=nombre, apellido=apellido, telefono=telefono)
        mesero.save()
        return redirect("meseros")
    return render(request, "restaurante/meseros/form.html")

def meseros_update(request, id):
    mesero = Mesero.objects.get(id=id)
    if request.method == "POST":
        mesero.nombre = request.POST.get("nombre")
        mesero.apellido = request.POST.get("apellido")
        mesero.telefono = request.POST.get("telefono")
        mesero.save()
        return redirect("meseros")
    return render(request, "restaurante/meseros/form.html", {"mesero": mesero})

def meseros_delete(request, id):
    mesero = Mesero.objects.get(id=id)
    mesero.delete()
    return redirect("meseros")