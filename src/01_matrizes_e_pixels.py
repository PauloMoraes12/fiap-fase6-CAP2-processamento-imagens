"""
FIAP - Data Science
Fase 6 | Capítulo 2 - Análise de Imagens

Laboratório 01: Matrizes e Pixels

Objetivo:
Compreender como imagens em escala de cinza
podem ser representadas por matrizes numéricas.
"""

import numpy as np

# 1. Criar uma matriz de pixels.
# Cada número representa uma intensidade de cinza.
imagem = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 2. Exibir a matriz original.
print("Matriz original:")
print(imagem)

# 3. Consultar as dimensões da matriz.
# O formato retornado é (linhas, colunas).
print("\nDimensões:", imagem.shape)

# 4. Acessar um pixel específico.
# Os índices começam em zero.
print("Pixel [1, 2]:", imagem[1, 2])

# 5. Modificar a intensidade de um pixel.
# Em imagens de 8 bits, 255 representa branco.
imagem[1, 2] = 255

# 6. Exibir a matriz após a alteração.
print("\nMatriz modificada:")
print(imagem)