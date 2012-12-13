# coding: utf-8
from __future__ import division


class Contador(object):

    def __init__(self):
        self.valores = []

    def incrementar(self, items):
        self.valores.extend(list(items))

    def contagem(self, item):
        valor = self.valores.count(item)
        if not valor:
            raise KeyError(item)
        return valor


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
