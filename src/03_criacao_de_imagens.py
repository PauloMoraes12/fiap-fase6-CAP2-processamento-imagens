
"""
FIAP — Fase 6 | Capítulo 2
Laboratório 03 — Criação e Visualização de Imagens

Objetivo:
Criar imagens RGB e em escala de cinza utilizando
NumPy e visualizá-las com Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


# 1. Criando uma imagem RGB preta
imagem_preta = np.zeros((3, 3, 3), dtype=np.uint8)

print("Imagem preta:")
print(imagem_preta)
print("Shape:", imagem_preta.shape)
print("Ndim:", imagem_preta.ndim)


# 2. Criando uma imagem RGB branca
imagem_branca = np.ones((3, 3, 3), dtype=np.uint8) * 255

print("\nImagem branca:")
print(imagem_branca)


# 3. Criando uma imagem em escala de cinza
imagem_cinza = np.array([
    [0, 128],
    [200, 255]
], dtype=np.uint8)

print("\nImagem em escala de cinza:")
print(imagem_cinza)
print("Shape:", imagem_cinza.shape)
print("Ndim:", imagem_cinza.ndim)


# 4. Visualizando as três imagens
fig, eixos = plt.subplots(1, 3, figsize=(10, 4))

eixos[0].imshow(imagem_preta)
eixos[0].set_title("Imagem preta")

eixos[1].imshow(imagem_branca)
eixos[1].set_title("Imagem branca")

eixos[2].imshow(
    imagem_cinza,
    cmap="gray",
    vmin=0,
    vmax=255
)
eixos[2].set_title("Escala de cinza")

# Removendo os eixos para destacar os pixels
for eixo in eixos:
    eixo.axis("off")

plt.tight_layout()
plt.show()
