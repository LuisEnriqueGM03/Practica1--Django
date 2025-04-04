from django.urls import path

from . import  views

urlpatterns = [
    path("clientes/", views.clientes_list, name="clientes"),
    path("clientes/create/", views.clientes_create, name="clientes_create"),
    path("clientes/update/<int:id>/", views.clientes_update, name="clientes_update"),
    path("clientes/delete/<int:id>/", views.clientes_delete, name="clientes_delete"),

    path("mesas/", views.mesas_list, name="mesas"),
    path("mesas/create/", views.mesas_create, name="mesas_create"),
    path("mesas/update/<int:id>/", views.mesas_update, name="mesas_update"),
    path("mesas/delete/<int:id>/", views.mesas_delete, name="mesas_delete"),


    path('platos/', views.platos_list, name='platos'),
    path('platos/create/', views.platos_create, name='platos_create'),
    path('platos/update/<int:id>/', views.platos_update, name='platos_update'),
    path('platos/delete/<int:id>/', views.platos_delete, name='platos_delete'),


    path('meseros/', views.meseros_list, name='meseros'),
    path('meseros/crear/', views.meseros_create, name='meseros_create'),
    path('meseros/editar/<int:id>/', views.meseros_update, name='meseros_update'),
    path('meseros/eliminar/<int:id>/', views.meseros_delete, name='meseros_delete'),

    path("ordenes/", views.ordenes_list, name="ordenes"),
    path("ordenes/create/", views.ordenes_create, name="ordenes_create"),
    path("ordenes/update/<int:id>/", views.ordenes_update, name="ordenes_update"),
    path("ordenes/delete/<int:id>/", views.ordenes_delete, name="ordenes_delete"),

    path("orden_platos/", views.orden_platos_list, name="orden_platos"),
    path("orden_platos/create/", views.orden_platos_create, name="orden_platos_create"),
    path("orden_platos/update/<int:id>/", views.orden_platos_update, name="orden_platos_update"),
    path("orden_platos/delete/<int:id>/", views.orden_platos_delete, name="orden_platos_delete"),
    path("ordenes/pagar/<int:id>/", views.ordenes_pagar, name="ordenes_pagar"),

]
