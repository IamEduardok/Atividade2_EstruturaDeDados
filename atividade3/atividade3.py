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

    def inorder(self):
        return self._inorder(self.raiz)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.esquerda) + [node.valor] + self._inorder(node.direita)

    def preorder(self):
        return self._preorder(self.raiz)

    def _preorder(self, node):
        if node is None:
            return []
        return [node.valor] + self._preorder(node.esquerda) + self._preorder(node.direita)

    def postorder(self):
        return self._postorder(self.raiz)

    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.esquerda) + self._postorder(node.direita) + [node.valor]

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

# Árvore com valores fixos
valores_fixos = [55, 30, 80, 20, 45, 70, 90]
bst_fixa = BinarySearchTree()
for v in valores_fixos:
    bst_fixa.insert(v)

bst_fixa.visualizar("arvore_fixa")

print("\n--- Travessias da Árvore Fixa ---")
print("In-Order   (E-R-D):", bst_fixa.inorder())
print("Pre-Order  (R-E-D):", bst_fixa.preorder())
print("Post-Order (E-D-R):", bst_fixa.postorder())

# Árvore com valores randômicos
valores_aleatorios = random.sample(range(1, 201), 10)
bst_aleatoria = BinarySearchTree()
for v in valores_aleatorios:
    bst_aleatoria.insert(v)

bst_aleatoria.visualizar("arvore_aleatoria")

print("\n--- Travessias da Árvore Aleatória ---")
print("Valores inseridos:", valores_aleatorios)
print("In-Order   (E-R-D):", bst_aleatoria.inorder())
print("Pre-Order  (R-E-D):", bst_aleatoria.preorder())
print("Post-Order (E-D-R):", bst_aleatoria.postorder())