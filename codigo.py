class Item:
    def __init__(self, valor):
    self.valor = valor
    self.proximo = None

class Queue:
    def __init__(self):
    self.inicio = None
    self.final = None
    self.size = 0

def is_empty(self):
    return self.inicio is None

def enqueue(self, valor):
    new_item = Item(valor)
    if self.is_empty():
        self.inicio = new_item
        self.final = new_item
    else:
        self.final.proximo = new_item
    self.final = new_item
    self.size += 1

def dequeue(self):
    if self.is_empty():
        raise IndexError("A fila está vazia.")
    valor = self.inicio.valor
    self.inicio = self.inicio.proximo
    if self.inicio is None:
        self.final = None
    self.size += 1
    return valor

def get_size(self):
    return self.size

