# coding: utf-8

from .serializer import DadosPessoaisSerializer
from .models import DadosPessoais

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from django.shortcuts import render

# Codigo do projeto antigo

def portfolio_exibir(request):
    pessoa = DadosPessoais.objects.all()
    context = {'pessoa': pessoa}

    return render(request, 'portfolios/portfolio_exibir.html', context)


'''
-- Primeiro Código --
class PortfolioViewSet(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)
'''

'''
-- Segundo Código --
class PortfolioViewSet(APIView):

    def get(self, request, pk, format=None):
        if not DadosPessoais.objects.filter(pk=pk).exists():
            dados_pessoais = DadosPessoaisSerializer([])
        else:
            dados_pessoais = DadosPessoais.objects.get(pk=pk)
            serializer = DadosPessoaisSerializer(dados_pessoais)

        return Response(serializer.data)


class PortfolioListViewSet(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        _category = self.request.query_params.get('category', None)

        if _category:
            queryset = DadosPessoais.objects.filter(category__id=_category)
        else:
            queryset = DadosPessoais.objects.all()

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
'''


class PortfolioViewSet(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "403 Forbidden"}, status=status.HTTP_409_CONFLICT)


class PortfolioUpdateView(APIView):

    def get(self, request, pk, format=None):
        user = DadosPessoais.objects.get(pk=pk)
        serializer = DadosPessoaisSerializer(user)
        return Response(serializer.data)

    def post(self, request, pk=None):
        user = DadosPessoais.objects.get(pk=pk)
        serializer = DadosPessoaisSerializer(data=request.data, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
