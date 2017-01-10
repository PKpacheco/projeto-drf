# coding: utf-8

from .serializer import DadosPessoaisSerializer
from .models import DadosPessoais

from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryViewSet(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)
