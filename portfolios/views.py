# coding: utf-8

from .serializer import DadosPessoaisSerializer
from .models import DadosPessoais

from rest_framework.response import Response
from rest_framework.views import APIView


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
