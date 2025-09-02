import random
from graphviz import Digraph

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BinarySearchTree:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        self.raiz = self._insert(self.raiz, valor)

    def _insert(self, node, valor):
        if node is None:
            return Node(valor)
        if valor < node.valor:
            node.esquerda = self._insert(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = self._insert(node.direita, valor)
        return node

    def search(self, valor):
        return self._search(self.raiz, valor)

    def _search(self, node, valor):
        if node is None:
            return False
        if valor == node.valor:
            return True
        if valor < node.valor:
            return self._search(node.esquerda, valor)
        else:
            return self._search(node.direita, valor)

    def delete(self, valor):
        self.raiz = self._delete(self.raiz, valor)

    def _delete(self, node, valor):
        if node is None:
            return None
        if valor < node.valor:
            node.esquerda = self._delete(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = self._delete(node.direita, valor)
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            temp = self._min_value_node(node.direita)
            node.valor = temp.valor
            node.direita = self._delete(node.direita, temp.valor)
        return node

    def _min_value_node(self, node):
        atual = node
        while atual.esquerda:
            atual = atual.esquerda
        return atual

    def height(self):
        return self._height(self.raiz)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.esquerda), self._height(node.direita))

    def depth(self, valor):
        return self._depth(self.raiz, valor, 0)

    def _depth(self, node, valor, nivel):
        if node is None:
            return -1
        if valor == node.valor:
            return nivel
        if valor < node.valor:
            return self._depth(node.esquerda, valor, nivel + 1)
        else:
            return self._depth(node.direita, valor, nivel + 1)

    def visualizar(self, nome_arquivo):
        dot = Digraph()
        self._visualizar(self.raiz, dot)
        dot.render(nome_arquivo, format='png', cleanup=True)

    def _visualizar(self, node, dot):
        if node:
            dot.node(str(node.valor))
            if node.esquerda:
                dot.edge(str(node.valor), str(node.esquerda.valor))
                self._visualizar(node.esquerda, dot)
            if node.direita:
                dot.edge(str(node.valor), str(node.direita.valor))
                self._visualizar(node.direita, dot)

# Demonstração com valores fixos
valores_fixos = [55, 30, 80, 20, 45, 70, 90]
bst_fixa = BinarySearchTree()
for v in valores_fixos:
    bst_fixa.insert(v)

bst_fixa.visualizar("arvore_fixa")

print("Busca pelo valor 45:", bst_fixa.search(45))
bst_fixa.delete(30)
bst_fixa.insert(60)
bst_fixa.visualizar("arvore_fixa_atualizada")

print("Altura da árvore fixa:", bst_fixa.height())
print("Profundidade do nó 45:", bst_fixa.depth(45))

# Demonstração com valores aleatórios
valores_aleatorios = random.sample(range(1, 201), 15)
bst_aleatoria = BinarySearchTree()
for v in valores_aleatorios:
    bst_aleatoria.insert(v)

bst_aleatoria.visualizar("arvore_aleatoria")

print("Valores aleatórios inseridos:", valores_aleatorios)
print("Altura da árvore aleatória:", bst_aleatoria.height())