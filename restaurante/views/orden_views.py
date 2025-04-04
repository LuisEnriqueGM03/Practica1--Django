from django.shortcuts import render, redirect
from django.contrib import messages
from restaurante.models import Orden, OrdenPlato, Plato, Mesa, Mesero,Cliente


def ordenes_list(request):
    ordenes = Orden.objects.all()
    return render(request, "restaurante/ordenes/list.html", {"ordenes": ordenes})


def ordenes_create(request):
    if request.method == "POST":
        mesero_id = request.POST.get("mesero")
        mesa_id = request.POST.get("mesa")
        platos_ids = request.POST.getlist("platos")
        cantidades = request.POST.getlist("cantidades")

        mesa = Mesa.objects.get(id=mesa_id)
        if Orden.objects.filter(mesa=mesa, estado='abierto').exists():
            messages.error(request, "La mesa seleccionada ya tiene una orden abierta.")
            return redirect("ordenes_create")

        mesero = Mesero.objects.get(id=mesero_id)
        orden = Orden.objects.create(mesero=mesero, mesa=mesa, cliente=None, estado='abierto')

        for plato_id, cantidad in zip(platos_ids, cantidades):
            plato = Plato.objects.get(id=plato_id)
            OrdenPlato.objects.create(orden=orden, plato=plato, cantidad=int(cantidad))

        return redirect("ordenes")

    meseros = Mesero.objects.all()
    mesas = Mesa.objects.all()
    platos = Plato.objects.all()
    return render(request, "restaurante/ordenes/form.html", {"meseros": meseros, "mesas": mesas, "platos": platos})


def ordenes_update(request, id):
    orden = Orden.objects.get(id=id)
    if request.method == "POST":
        mesero_id = request.POST.get("mesero")
        mesa_id = request.POST.get("mesa")
        platos_ids = request.POST.getlist("platos")
        cantidades = request.POST.getlist("cantidades")

        mesero = Mesero.objects.get(id=mesero_id)
        mesa = Mesa.objects.get(id=mesa_id)

        if mesa != orden.mesa and Orden.objects.filter(mesa=mesa, estado='abierto').exists():
            return redirect("ordenes_update", id=id)

        orden.mesero = mesero
        orden.mesa = mesa
        orden.estado = request.POST.get("estado", orden.estado)
        orden.save()

        orden.orden_platos.all().delete()
        for plato_id, cantidad in zip(platos_ids, cantidades):
            plato = Plato.objects.get(id=plato_id)
            OrdenPlato.objects.create(orden=orden, plato=plato, cantidad=int(cantidad))

        return redirect("ordenes")

    meseros = Mesero.objects.all()
    mesas = Mesa.objects.all()
    platos = Plato.objects.all()
    return render(request, "restaurante/ordenes/form.html", {
        "orden": orden,
        "meseros": meseros,
        "mesas": mesas,
        "platos": platos
    })

def ordenes_pagar(request, id):
    orden = Orden.objects.get(id=id)

    if request.method == "POST":
        cliente_id = request.POST.get("cliente")
        if cliente_id:
            cliente = Cliente.objects.get(id=cliente_id)
            orden.cliente = cliente
        else:
            orden.cliente = None
        orden.estado = 'cerrado'
        orden.save()
        return redirect("ordenes")

    clientes = Cliente.objects.all()
    return render(request, "restaurante/ordenes/formPagar.html", {
        "orden": orden,
        "clientes": clientes
    })


def ordenes_delete(request, id):
    orden = Orden.objects.get(id=id)
    orden.delete()
    return redirect("ordenes")
