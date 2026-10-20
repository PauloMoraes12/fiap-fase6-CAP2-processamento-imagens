
import numpy as np

# Criando um pixel com três canais de cores:
# R = vermelho, G = verde, B = azul
pixel = np.array([255, 0, 0])

print("Pixel original:", pixel)

# Acessando cada canal individualmente
print("Vermelho:", pixel[0])
print("Verde:", pixel[1])
print("Azul:", pixel[2])

# Modificando a cor do pixel
# Adicionamos verde para transformar vermelho em amarelo
pixel[1] = 255

print("Pixel modificado:", pixel)


# Criando uma imagem RGB com 2 linhas e 2 colunas
imagem = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 0]]
])

print("\nImagem RGB:")
print(imagem)

# Verificando as dimensões da imagem
print("\nFormato da imagem:", imagem.shape)



# Criando uma imagem RGB de 2 linhas e 2 colunas
imagem_teste = np.array([
    [[255, 100, 50], [100, 200, 255]],
    [[50, 150, 200], [200, 100, 150]]
])

print("Imagem antes:")
print(imagem_teste)

# Zerando o canal azul de todos os pixels
imagem_teste[:, :, 2] = 0

print("\nImagem depois:")
print(imagem_teste)



import matplotlib.pyplot as plt

# Exibindo a imagem original e a modificada
fig, eixos = plt.subplots(1, 2, figsize=(8, 4))

eixos[0].imshow(np.array([
    [[255, 100, 50], [100, 200, 255]],
    [[50, 150, 200], [200, 100, 150]]
], dtype=np.uint8))
eixos[0].set_title("Imagem original")
eixos[0].axis("off")

eixos[1].imshow(imagem_teste.astype(np.uint8))
eixos[1].set_title("Sem canal azul")
eixos[1].axis("off")

plt.tight_layout()
plt.show()



# Criando uma imagem em escala de cinza
imagem_cinza = np.array([
    [0, 128],
    [200, 255]
], dtype=np.uint8)

# Visualizando a imagem
plt.imshow(imagem_cinza, cmap="gray", vmin=0, vmax=255)
plt.title("Minha primeira imagem em escala de cinza")
plt.colorbar(label="Intensidade")
plt.show()


