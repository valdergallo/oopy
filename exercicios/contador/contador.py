# coding: utf-8
from __future__ import division
from collections import Counter


"""
Código inicial usado na Lista de Exercícios 1 do curso
"Objetos Pythonicos" de Luciano Ramalho, Oficinas Turing.
"""


class Contador(object):

    def __init__(self):
        self.valores = []
        self.ocorrencias = {}

    def incrementar(self, items):
        self.valores.extend(list(items))

    def contagem(self, item):
        self.ocorrencias = dict(Counter(self.valores))
        return self.ocorrencias[item]


class ContadorAmigavel(Contador):

    def __init__(self):
        self.valores = []

    def contagem(self, item):
        return self.valores.count(item)


class ContadorTotalizador(Contador):

    def __init__(self):
        super(ContadorTotalizador, self).__init__()
        self.total = 0

    def incrementar(self, items):
        super(ContadorTotalizador, self).incrementar(items)
        self.total = len(self.valores)

    def porcentagem(self, item):
        return (self.valores.count(item) / self.total) * 100


class ContadorTotalizadorAmigavel(ContadorAmigavel, ContadorTotalizador):
    pass
