from django.shortcuts import render, redirect
from restaurante.models import OrdenPlato, Orden, Plato


def orden_platos_list(request):
    orden_platos = OrdenPlato.objects.all()
    return render(request, "restaurante/ordenesPlatos/list.html", {"orden_platos": orden_platos})


def orden_platos_create(request):
    if request.method == "POST":
        orden_id = request.POST.get("orden")
        plato_id = request.POST.get("plato")
        cantidad = request.POST.get("cantidad")

        orden = Orden.objects.get(id=orden_id)
        plato = Plato.objects.get(id=plato_id)

        OrdenPlato.objects.create(orden=orden, plato=plato, cantidad=int(cantidad))

        return redirect("orden_platos_list")

    ordenes = Orden.objects.all()
    platos = Plato.objects.all()
    return render(request, "restaurante/ordenesPlatos/form.html", {"ordenes": ordenes, "platos": platos})


def orden_platos_update(request, id):
    orden_plato = OrdenPlato.objects.get(id=id)
    if request.method == "POST":
        orden_plato.cantidad = request.POST.get("cantidad")
        orden_plato.save()
        return redirect("orden_platos")
    return render(request, "restaurante/ordenesPlatos/form.html", {"orden_plato": orden_plato})


def orden_platos_delete(request, id):
    orden_plato = OrdenPlato.objects.get(id=id)
    orden_plato.delete()
    return redirect("orden_platos")
