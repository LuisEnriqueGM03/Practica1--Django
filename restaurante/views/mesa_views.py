from django.shortcuts import render, redirect
from restaurante.models import Mesa

def mesas_list(request):
    mesas = Mesa.objects.all()
    return render(request, "restaurante/mesas/list.html", {"mesas": mesas})

def mesas_create(request):
    if request.method == "POST":
        numero = request.POST.get("numero")
        mesa = Mesa(numero=numero)
        mesa.save()
        return redirect("mesas")
    return render(request, "restaurante/mesas/form.html")

def mesas_update(request, id):
    mesa = Mesa.objects.get(id=id)
    if request.method == "POST":
        mesa.numero = request.POST.get("numero")
        mesa.save()
        return redirect("mesas")
    return render(request, "restaurante/mesas/form.html", {"mesa": mesa})

def mesas_delete(request, id):
    mesa = Mesa.objects.get(id=id)
    mesa.delete()
    return redirect("mesas")