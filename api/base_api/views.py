from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Montadora, Modelo
from .serializers import ModeloSerializer, MontadoraSerializer
from django.db.models import Q

@api_view(['GET'])
def endpoints(request):
    data = ['/modelos', 'modelos/:nome' ]
    return Response(data)

# Modelos
@api_view(['GET','POST'])
def lista_modelos(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''
        
        modelos = Modelo.objects.filter(Q (nome__icontains=query) | Q(descricao__icontains=query) | Q(montadora__nome__icontains=query))
        serializer = ModeloSerializer(modelos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        montadora_nome = request.data['montadora']
        montadora = get_object_or_404(Montadora, nome=montadora_nome) 

        modelo = Modelo.objects.create(
            nome=request.data['nome'],
            descricao=request.data['descricao'],
            montadora=montadora,
        )

        serializer = ModeloSerializer(modelo, many=False)
        return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
def modelo_unico(request, nome):
    modelo = get_object_or_404(Modelo, nome=nome)

    if request.method == 'GET':
        serializer = ModeloSerializer(modelo, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        montadora_nome = request.data['montadora']
        montadora = get_object_or_404(Montadora, nome=montadora_nome)

        modelo.nome = request.data['nome']
        modelo.descricao = request.data['descricao']
        modelo.montadora = montadora

        modelo.save()
        serializer = ModeloSerializer(modelo, many=False)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        modelo.delete()
        return Response('Modelo deletado.')
    
# Montadoras    
@api_view(['GET','POST'])
def lista_montadoras(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''
        
        montadoras = Montadora.objects.filter(Q(nome__icontains=query) | Q(bio__icontains=query))
        serializer = MontadoraSerializer(montadoras, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        montadoras = Montadora.objects.create(
            nome=request.data['nome'],
            bio=request.data['bio'],
        )

        serializer = MontadoraSerializer(montadoras, many=False)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def montadora_unica(request, nome):
    montadora = Montadora.objects.get(nome=nome)

    if request.method == 'GET':
        serializer = MontadoraSerializer(montadora, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        montadora.nome=request.data['nome']
        montadora.bio=request.data['bio']

        montadora.save()
        serializer = MontadoraSerializer(montadora, many=False)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        montadora.delete()
        return Response('Montadora deletada.')