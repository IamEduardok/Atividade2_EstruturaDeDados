import random
from graphviz import Digraph

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVLTree:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        self.raiz = self._insert(self.raiz, valor)

    def _insert(self, node, valor):
        if not node:
            return Node(valor)
        if valor < node.valor:
            node.esquerda = self._insert(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = self._insert(node.direita, valor)
        else:
            return node  # valores duplicados não são inseridos

        node.altura = 1 + max(self._get_altura(node.esquerda), self._get_altura(node.direita))
        balance = self._get_balance(node)

        # Rotação simples à direita
        if balance > 1 and valor < node.esquerda.valor:
            return self._rotate_right(node)

        # Rotação simples à esquerda
        if balance < -1 and valor > node.direita.valor:
            return self._rotate_left(node)

        # Rotação dupla esquerda-direita
        if balance > 1 and valor > node.esquerda.valor:
            node.esquerda = self._rotate_left(node.esquerda)
            return self._rotate_right(node)

        # Rotação dupla direita-esquerda
        if balance < -1 and valor < node.direita.valor:
            node.direita = self._rotate_right(node.direita)
            return self._rotate_left(node)

        return node

    def _get_altura(self, node):
        return node.altura if node else 0

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_altura(node.esquerda) - self._get_altura(node.direita)

    def _rotate_left(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def _rotate_right(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

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

# Demonstração com valores fixos (rotação simples)
print("\n--- Inserção: [10, 20, 30] ---")
avl_simples = AVLTree()
for i, v in enumerate([10, 20, 30], start=1):
    avl_simples.insert(v)
    avl_simples.visualizar(f"avl_simples_{i}")

# Demonstração com valores fixos (rotação dupla)
print("\n--- Inserção: [10, 30, 20] ---")
avl_dupla = AVLTree()
for i, v in enumerate([10, 30, 20], start=1):
    avl_dupla.insert(v)
    avl_dupla.visualizar(f"avl_dupla_{i}")

# Árvore com valores randômicos
valores_aleatorios = random.sample(range(1, 201), 20)
avl_aleatoria = AVLTree()
for v in valores_aleatorios:
    avl_aleatoria.insert(v)

avl_aleatoria.visualizar("avl_aleatoria")

print("\n--- Árvore AVL com valores aleatórios ---")
print("Valores inseridos:", valores_aleatorios)