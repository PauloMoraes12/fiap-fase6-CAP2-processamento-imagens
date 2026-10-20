
"""
FIAP — Fase 6 | Capítulo 2
Laboratório 04 — Fatiamento de Imagens

Objetivo:
Selecionar e modificar linhas, colunas,
canais e regiões de uma imagem RGB.
"""

import numpy as np
import matplotlib.pyplot as plt


# 1. Criando uma imagem preta de 5 x 5 pixels
imagem = np.zeros((5, 5, 3), dtype=np.uint8)

# 2. Primeira linha vermelha
imagem[0, :, 0] = 255

# 3. Última linha verde
imagem[4, :, 1] = 255

# 4. Terceira coluna azul
imagem[:, 2, 2] = 255

# 5. Pixel central branco
imagem[2, 2, :] = 255

print("Matriz RGB:")
print(imagem)

print("\nFormato:", imagem.shape)
print("Dimensões:", imagem.ndim)


# 6. Visualizando o resultado
fig, ax = plt.subplots(figsize=(7, 7))

ax.imshow(imagem, interpolation="nearest")
ax.set_title("Laboratório 04 — Fatiamento de Imagens", pad=18)

ax.set_xticks(range(5))
ax.set_yticks(range(5))

ax.set_xlabel("Colunas")
ax.set_ylabel("Linhas")

ax.set_xticks(np.arange(-0.5, 5, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 5, 1), minor=True)
ax.grid(which="minor", color="gray", linewidth=1)

ax.tick_params(which="minor", bottom=False, left=False)

plt.tight_layout()
plt.show()
