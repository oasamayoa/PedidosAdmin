#from django
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

#from models
from productos.models import Producto

#from others
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


class HomeView(View):
    def get(self , request , *args , **kwargs):
        return render(request, 'productos/charts.html', {})

def get_data(request , *args , **kwards):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class CharData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        users = User.objects.all().count()
        products = Producto.objects.all().count()
        labels = ['Vendedores', 'Productos', 'Prueba', 'Otros2', 'Purple', 'Orange']
        default_items = [users, products, 5, 8, 11, 12]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
