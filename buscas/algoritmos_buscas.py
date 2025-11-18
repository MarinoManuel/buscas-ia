import heapq
from . import dados


def ids(inicio, objectivo, tempo):
    grafo = dados.carregar_grafo()
    visitados = set()
    tempo_minimo_profundidade = []
    heapq.heappush(tempo_minimo_profundidade, float('inf'))
    def dfs_limitado(vertice, limite, caminho, tempo_caminho):
        visitados.add(vertice)
        if (vertice != inicio):
            if vertice == objectivo:
                tempo_ultimo_vertice = dados.calcular_tempo_vizinho(caminho[-1], vertice)
                if tempo_ultimo_vertice == 0:
                    return False
                tempo_vertice_acumulado = tempo_caminho[ caminho[-1] ] + tempo_ultimo_vertice
                caminho.append(vertice)
                tempo_caminho[ vertice ] = tempo_vertice_acumulado
                return True
            if limite == 0:
                tempo_ultimo_vertice = dados.calcular_tempo_vizinho(caminho[-1], vertice)
                if tempo_ultimo_vertice != 0:
                    tempo_vertice_acumulado = tempo_caminho[caminho[-1]] + tempo_ultimo_vertice
                    heapq.heappush(tempo_minimo_profundidade, tempo_vertice_acumulado )
                return False
            tempo_ultimo_vertice = dados.calcular_tempo_vizinho(caminho[-1], vertice)
            if (tempo_ultimo_vertice == 0):
                return False
            tempo_vertice_acumulado = tempo_caminho[caminho[-1]] + tempo_ultimo_vertice
            caminho.append(vertice)
            tempo_caminho[vertice] = tempo_vertice_acumulado
        if (limite == 0 and vertice == inicio):
            heapq.heappush(tempo_minimo_profundidade, 0)
            return False
        for vizinho in grafo[vertice]:
            if vizinho not in caminho:
                if (dfs_limitado(vizinho, limite - 1, caminho, tempo_caminho)):
                    return True
        if vertice != inicio:
            ultimo = caminho.pop()
            tempo_caminho.pop(ultimo)
        return False
    limite = 0
    while True:
        caminho = [inicio]
        tempo_caminho = {inicio : 0}
        if dfs_limitado(inicio, limite, caminho, tempo_caminho):
            return tempo_caminho[caminho[-1]], caminho, visitados

        if(heapq.heappop(tempo_minimo_profundidade) > tempo):
            return tempo_caminho[caminho[-1]], caminho, visitados
        limite += 1

        tempo_minimo_profundidade.clear()
        heapq.heappush(tempo_minimo_profundidade, float('inf'))

def ucs(inicio, objectivo):
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
                    tempo_vizinho = dados.calcular_tempo_vizinho(vertice, vizinho)
                    if tempo_vizinho == 0:
                        continue
                    tempo_vizinho_acumulado = tempo_acumulado + tempo_vizinho
                    heapq.heappush(fila, (tempo_vizinho_acumulado, vizinho, caminho + [vizinho]) )

def ass(inicio, objectivo):
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
                tempo_vizinho = dados.calcular_tempo_vizinho(vertice, vizinho)
                if tempo_vizinho == 0:
                    continue
                tempo_vizinho_acumulado = tempo_acumulado + tempo_vizinho
                f_heuristica = tempo_vizinho_acumulado + heuristicas[vizinho]
                heapq.heappush(fila, (f_heuristica, tempo_vizinho_acumulado, vizinho, caminho + [vizinho]) )
