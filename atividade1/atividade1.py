# atividade_1.py

from graphviz import Digraph
import random

# Função para construir a árvore fixa: (7 + 3) * (5 - 2)
def construir_arvore_fixa():
    dot = Digraph(comment='Árvore Fixa')
    
    # Nós
    dot.node('A', '*')
    dot.node('B', '+')
    dot.node('C', '-')
    dot.node('D', '7')
    dot.node('E', '3')
    dot.node('F', '5')
    dot.node('G', '2')

    # Conexões
    dot.edge('A', 'B')
    dot.edge('A', 'C')
    dot.edge('B', 'D')
    dot.edge('B', 'E')
    dot.edge('C', 'F')
    dot.edge('C', 'G')

    # Salvar e renderizar
    dot.render('arvore_fixa', format='png', cleanup=True)
    print("✅ Imagem da árvore fixa gerada: arvore_fixa.png")

# Função para gerar expressão aleatória e construir árvore
def construir_arvore_aleatoria():
    operadores = ['+', '-', '*', '/']
    operandos = [str(random.randint(1, 9)) for _ in range(3)]
    ops = random.sample(operadores, 2)

    expr = f"( {operandos[0]} {ops[0]} {operandos[1]} ) {ops[1]} {operandos[2]}"
    print(f"\nExpressão aleatória: {expr}")

    dot = Digraph(comment='Árvore Aleatória')

    # Nós
    dot.node('A', ops[1])
    dot.node('B', ops[0])
    dot.node('C', operandos[0])
    dot.node('D', operandos[1])
    dot.node('E', operandos[2])

    # Conexões
    dot.edge('A', 'B')
    dot.edge('A', 'E')
    dot.edge('B', 'C')
    dot.edge('B', 'D')

    # Salvar e renderizar
    dot.render('arvore_aleatoria', format='png', cleanup=True)
    print("✅ Imagem da árvore aleatória gerada: arvore_aleatoria.png")

# Executar
if __name__ == "__main__":
    construir_arvore_fixa()
    construir_arvore_aleatoria()