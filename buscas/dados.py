import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_custos = os.path.join(BASE_DIR, "custos.txt")
path_grafo = os.path.join(BASE_DIR, "grafo.txt")

def carregar_custos():
    with open(path_custos, "r") as f:
        dados = json.load(f)
    custos = {frozenset(k.split(',')): tuple(v) for k, v in dados.items()}
    return custos

def ler_custo(a, b, custos):
    return custos.get(frozenset({a, b}))


def carregar_grafo():
    with open(path_grafo, "r") as f:
        dados = json.load(f)
    return {k: set(v) for k, v in dados.items()}


def carregar_heuristica(nome_arquivo):
    with open( os.path.join(BASE_DIR, 'h_' + nome_arquivo + '.txt') , "r") as f:
        heuristica = json.load(f)
    return heuristica

