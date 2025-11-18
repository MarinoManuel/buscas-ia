from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .algoritmos_buscas import ucs, ass, ids


class BuscaView(APIView):

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        origem = request.data.get('origem')
        destino = request.data.get('destino')
        algoritmo = request.data.get('algoritmo')
        tempo_limite = float(request.data.get('tempo'))

        escolha_algoritmo = {
            'A': ass,
            'CU': ucs,
            'BP':ids
        }
        if(algoritmo != 'BP'):
            resultado = escolha_algoritmo[algoritmo](origem, destino)
        else:
            resultado = escolha_algoritmo[algoritmo](origem, destino, tempo_limite)
        dados = {}
        dados['tempo'] = resultado[0]
        dados['caminho'] = resultado[1]
        dados['nos_visitados'] = resultado[2]
        return Response(dados)





