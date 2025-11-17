import heapq
from . import dados


def ucs(inicio, objectivo):
    custos = dados.carregar_custos()
    grafo = dados.carregar_grafo()
    visitados = set()
    fila = [(0, inicio, [inicio])] # tempo, vertice, caminho
    while fila:
        tempo_acumulado, vertice, caminho = heapq.heappop(fila)
        if vertice not in visitados:
            visitados.add(vertice)
            if vertice == objectivo:
                return tempo_acumulado, caminho, visitados
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    distancia_vizinho, congestionamento, condicao_estrada, velocidade_ideal = dados.ler_custo(vertice, vizinho, custos)
                    velocidade_real = velocidade_ideal * congestionamento * condicao_estrada
                    if velocidade_real == 0:
                        continue
                    tempo_vizinho = distancia_vizinho/velocidade_real
                    tempo_vizinho_acumulado = tempo_acumulado + tempo_vizinho
                    heapq.heappush(fila, (tempo_vizinho_acumulado, vizinho, caminho + [vizinho]) )


def ass(inicio, objectivo):
    custos = dados.carregar_custos()
    grafo = dados.carregar_grafo()
    heuristicas = dados.carregar_heuristica(objectivo)
    visitados = set()
    fila = [(0 + heuristicas[inicio], 0, inicio, [inicio])] # f(n) = g(n) + h(n), tempo ate n,vertice, caminho
    while fila:
        _ , tempo_acumulado, vertice, caminho = heapq.heappop(fila)

        if vertice in visitados:
            continue
        visitados.add(vertice)
        if vertice == objectivo:
            return tempo_acumulado, caminho, visitados
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                distancia_vizinho, congestionamento, condicao_estrada, velocidade_ideal = dados.ler_custo(vertice,
                                                                                                          vizinho,
                                                                                                          custos)
                velocidade_real = velocidade_ideal * congestionamento * condicao_estrada
                if velocidade_real == 0:
                    continue
                tempo_vizinho = distancia_vizinho / velocidade_real
                tempo_vizinho_acumulado = tempo_acumulado + tempo_vizinho
                f_heuristica = tempo_vizinho_acumulado + heuristicas[vizinho]
                heapq.heappush(fila, (f_heuristica, tempo_vizinho_acumulado, vizinho, caminho + [vizinho]) )

