
# Diário de Aprendizado — FIAP Fase 6

## Capítulo 2 — Introdução à Análise de Imagens

Este documento registra os conceitos estudados,
os exercícios desenvolvidos e os resultados obtidos
durante os laboratórios de processamento de imagens.


### Laboratório 01 — Matrizes e Pixels

**Status:** Concluído.

**Objetivo:** Compreender como uma imagem digital pode
ser representada por uma matriz de valores numéricos.

#### Conceitos aprendidos

- Pixel: menor unidade de uma imagem digital.
- Matriz: estrutura organizada em linhas e colunas.
- NumPy: biblioteca utilizada para trabalhar com arrays.
- Índices: no Python, começam em zero.
- `shape`: informa o formato da matriz.

#### Exemplo prático

```python
import numpy as np

imagem = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(imagem.shape)  # (3, 3)
print(imagem[1, 2])  # 60

imagem[1, 2] = 255
```

#### O que compreendi

Uma imagem pode ser representada por números organizados
em uma matriz. Para acessar um pixel, utilizamos sua
posição: primeiro a linha, depois a coluna.

O comando `imagem[1, 2]` acessa o elemento da segunda
linha e terceira coluna.

Também aprendi que podemos modificar um valor da matriz
atribuindo um novo número à posição desejada.

**Arquivo desenvolvido:** `src/01_matrizes_e_pixels.py`



### Laboratório 02 — Canais RGB

**Status:** Concluído.

**Objetivo:** Compreender como as cores são representadas
e modificadas em imagens digitais.

#### Conceitos aprendidos

- RGB significa Red (vermelho), Green (verde) e Blue (azul).
- Cada canal possui intensidade de 0 a 255 em imagens
  RGB de 8 bits por canal.
- Um pixel RGB possui três valores: `[R, G, B]`.
- O índice `0` representa o vermelho.
- O índice `1` representa o verde.
- O índice `2` representa o azul.
- Alterar um canal não modifica automaticamente os outros.
- A combinação dos canais determina a cor resultante.

#### Exemplos de cores

| Cor | Valores RGB |
|---|---|
| Preto | `[0, 0, 0]` |
| Branco | `[255, 255, 255]` |
| Vermelho | `[255, 0, 0]` |
| Verde | `[0, 255, 0]` |
| Azul | `[0, 0, 255]` |
| Amarelo | `[255, 255, 0]` |
| Ciano | `[0, 255, 255]` |
| Magenta | `[255, 0, 255]` |

#### Exemplo prático — Modificando um pixel

```python
import numpy as np

pixel = np.array([255, 0, 0])

# Aumentando o canal verde
pixel[1] = 255

print(pixel)  # [255 255 0] — amarelo
```

#### Exemplo prático — Modificando uma imagem

```python
imagem = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 0]]
])

print(imagem.shape)  # (2, 2, 3)

# Transformando o pixel azul em branco
imagem[1, 0] = [255, 255, 255]

# Zerando o canal azul de todos os pixels
imagem[:, :, 2] = 0
```

#### O que compreendi

Uma imagem RGB é uma matriz tridimensional, organizada
em altura, largura e canais de cor.

Para acessar um canal específico, utilizamos:

`imagem[linha, coluna, canal]`

O símbolo `:` permite selecionar todas as posições
de uma dimensão.

Também compreendi que modificar um canal altera a
combinação de cores, mas preserva os demais canais
quando eles não são explicitamente modificados.

**Arquivo desenvolvido:** `src/02_canais_rgb.py`



### Laboratório 03 — Criação e Visualização de Imagens

**Status:** Concluído. Código executado e visualização validada.

**Resultado:** Foram criadas e exibidas três imagens:
preta, branca e em escala de cinza, utilizando NumPy
e Matplotlib.

**Arquivo desenvolvido:** `src/03_criacao_de_imagens.py`

**Objetivo:** Aprender a criar imagens usando NumPy,
identificar suas dimensões e visualizar seus pixels.

#### Conceitos aprendidos

- `np.zeros()`: cria uma matriz preenchida com zeros.
- `np.ones()`: cria uma matriz preenchida com uns.
- `dtype=np.uint8`: armazena inteiros de 0 a 255.
- `shape`: informa o tamanho de cada dimensão.
- `ndim`: informa quantas dimensões existem.
- `plt.imshow()`: exibe uma imagem.
- `plt.show()`: apresenta a visualização.

#### Criando uma imagem preta

```python
import numpy as np

imagem = np.zeros((3, 3, 3), dtype=np.uint8)

print(imagem.shape)  # (3, 3, 3)
print(imagem.ndim)   # 3
```

A imagem possui 3 linhas, 3 colunas e 3 canais RGB.

Todos os pixels começam com `[0, 0, 0]`, ou seja,
preto.

#### Criando uma imagem branca

```python
imagem = np.ones((3, 3, 3), dtype=np.uint8) * 255
```

Cada pixel terá os valores `[255, 255, 255]`.

#### Criando uma imagem em escala de cinza

```python
imagem_cinza = np.array([
    [0, 128],
    [200, 255]
], dtype=np.uint8)

print(imagem_cinza.shape)  # (2, 2)
print(imagem_cinza.ndim)   # 2
```

Em uma imagem de escala de cinza, cada pixel pode ser
representado por um único valor de intensidade:

- 0: preto.
- 128: cinza intermediário.
- 255: branco.

#### Visualizando com Matplotlib

```python
import matplotlib.pyplot as plt

plt.imshow(imagem_cinza, cmap="gray", vmin=0, vmax=255)
plt.title("Imagem em escala de cinza")
plt.colorbar(label="Intensidade")
plt.show()
```

#### RGB versus escala de cinza

| Tipo | Exemplo de shape | Dimensões |
|---|---|---|
| RGB | `(100, 200, 3)` | 3 |
| Cinza | `(100, 200)` | 2 |

#### O que compreendi

O NumPy permite criar imagens como matrizes numéricas.

A função `shape` mostra a altura, a largura e,
quando presente, a dimensão dos canais.

A propriedade `ndim` informa o número de dimensões,
não a quantidade de pixels.

O Matplotlib transforma essas matrizes em
visualizações que podemos interpretar.

**Arquivo planejado:** `src/03_criacao_de_imagens.py`



### Laboratório 04 — Fatiamento de Imagens

**Status:** Concluído. Código executado e visualização validada.

**Resultado:** Foi criada uma imagem RGB de 5 × 5 pixels,
com linhas coloridas, uma coluna azul e um pixel central
branco. A visualização foi ajustada para melhorar a
separação dos pixels e a legibilidade dos eixos.

**Arquivo desenvolvido:** `src/04_fatiamento_de_imagens.py`

**Objetivo:** Aprender a selecionar e modificar pixels,
linhas, colunas, canais e regiões de uma imagem.

#### Conceitos aprendidos

Em uma imagem RGB, usamos:

`imagem[linha, coluna, canal]`

O símbolo `:` permite selecionar todas as posições
de uma dimensão ou trabalhar com intervalos.

#### Selecionando pixels e canais

| Código | Significado |
|---|---|
| `imagem[0, 0]` | Primeiro pixel |
| `imagem[1, 1, :]` | Todos os canais do pixel central |
| `imagem[:, :, 0]` | Canal vermelho da imagem inteira |
| `imagem[:, :, 1]` | Canal verde da imagem inteira |
| `imagem[:, :, 2]` | Canal azul da imagem inteira |
| `imagem[0, :, :]` | Primeira linha inteira |
| `imagem[:, 1, :]` | Segunda coluna inteira |

#### Exemplo prático — Modificando linhas e colunas

```python
import numpy as np

# Criando uma imagem preta de 3 x 3 pixels
imagem = np.zeros((3, 3, 3), dtype=np.uint8)

# Primeira linha vermelha
imagem[0, :, 0] = 255

# Terceira linha verde
imagem[2, :, 1] = 255

# Segunda coluna recebe azul
imagem[:, 1, 2] = 255

# Pixel central fica branco
imagem[1, 1, :] = 255

print(imagem)
```

#### Selecionando regiões

```python
# Selecionando as duas primeiras linhas
# e as duas primeiras colunas

imagem[0:2, 0:2, :] = 255
```

O intervalo `0:2` inclui os índices 0 e 1,
mas não inclui o índice 2.

Portanto, esse comando modifica uma região
de 2 linhas por 2 colunas, totalizando 4 pixels.

#### O que compreendi

O NumPy permite modificar partes específicas de
uma imagem sem precisar alterar cada pixel
individualmente.

Aprendi a selecionar linhas, colunas e canais
usando índices e o símbolo `:`.

Também compreendi que o fatiamento permite
trabalhar com regiões retangulares da imagem.

A ordem das operações importa: uma modificação
posterior pode alterar pixels já modificados.

**Arquivo planejado:** `src/04_fatiamento_de_imagens.py`


---

### Laboratório 05 — Explorando Imagens com Jupyter

**Status:** Concluído. Código executado e visualização validada.

**Objetivo:** Aprender a utilizar o Jupyter Notebook
dentro do VS Code para explorar e visualizar imagens.

#### Conceitos aprendidos

- Diferença entre arquivos `.py` e `.ipynb`.
- Utilização de células Code e Markdown.
- Seleção do kernel Python do ambiente `.venv`.
- Instalação e utilização do `ipykernel`.
- Execução de células com `Shift + Enter`.
- Visualização de imagens diretamente no notebook.
- Documentação dos resultados com Markdown.

#### Experimento realizado

Foi criada uma matriz NumPy de formato `(3, 3)`,
representando intensidades de pixels em escala de cinza.

A matriz foi visualizada com Matplotlib, utilizando
`imshow()`, `cmap="gray"`, `vmin=0`, `vmax=255`
e `colorbar()`.

#### Resultado

A imagem foi exibida corretamente dentro do notebook,
sem necessidade de abrir uma janela externa.

#### O que compreendi

O Jupyter Notebook permite combinar explicações,
código Python e resultados visuais em um mesmo arquivo.

Essa abordagem facilita a experimentação, a análise
de dados e a documentação dos exercícios.

**Arquivo desenvolvido:** `notebooks/01_exploracao_de_imagens.ipynb`

**Bibliotecas utilizadas:** NumPy, Matplotlib e ipykernel.



## Laboratório 06 — Processamento de Fotografias

### Objetivo
Aprender a carregar, analisar, transformar e salvar
uma fotografia real utilizando Python.

### Ferramentas
- Python
- NumPy
- Pillow
- Matplotlib
- Jupyter Notebook

### Atividades realizadas
1. Carregamento da fotografia paisagem.jpg.
2. Conversão da fotografia em matriz NumPy.
3. Identificação das dimensões (2336, 3504, 3).
4. Análise dos pixels e canais RGB.
5. Cálculo das médias dos canais de cores.
6. Conversão para escala de cinza.
7. Validação matemática da conversão.
8. Salvamento da imagem paisagem_cinza.png.

### Resultados
- Fotografia original: 2336 × 3504 pixels.
- Média do vermelho: 68,24.
- Média do verde: 82,54.
- Média do azul: 46,45.
- Pixel central RGB: [62, 111, 55].
- Intensidade de cinza do pixel central: 90.
- Imagem processada salva com sucesso.

### Conclusão
Aprendi a trabalhar com fotografias reais como
matrizes NumPy, analisar canais de cores, converter
imagens para escala de cinza e salvar resultados
sem modificar o arquivo original.



## Laboratório 07 — Recortes de Fotografias

### Objetivo
Aprender a recortar regiões específicas de fotografias
utilizando o fatiamento de matrizes NumPy.

### Ferramentas
- Python
- NumPy
- Pillow
- Matplotlib
- Jupyter Notebook

### Atividades realizadas
1. Carregamento da fotografia PAULO.jpeg.
2. Conversão da fotografia em matriz NumPy.
3. Identificação das dimensões da imagem.
4. Estudo das coordenadas de linhas e colunas.
5. Seleção da região do rosto por fatiamento.
6. Conversão do recorte em imagem Pillow.
7. Salvamento do arquivo PAULO_rosto.png.

### Resultados
- Imagem original: (1600, 1021, 3).
- Código do recorte: imagem[300:1000, 300:850].
- Dimensões do recorte: (700, 550, 3).
- Total de pixels do recorte: 385.000.
- Arquivo gerado: imagens/PAULO_rosto.png.

### Conceitos aprendidos
- O NumPy organiza imagens RGB em três dimensões.
- O fatiamento utiliza [linhas, colunas].
- O índice inicial é incluído.
- O índice final é excluído.
- Image.fromarray() converte uma matriz em imagem.
- Pillow utiliza dimensões na ordem (largura, altura).

### Conclusão
Aprendi a selecionar e salvar regiões de fotografias
reais utilizando Python e NumPy, preservando a
fotografia original.



## Laboratório 08 — Redimensionamento e Filtros

### Objetivo
Aprender a redimensionar fotografias e aplicar filtros
utilizando a biblioteca Pillow.

### Atividades realizadas
1. Carreguei a fotografia PAULO.jpeg.
2. Consultei suas dimensões originais: 1021 × 1600 pixels.
3. Redimensionei a fotografia para 510 × 800 pixels.
4. Comparei os métodos de interpolação NEAREST e LANCZOS.
5. Calculei as médias RGB das duas versões:
   - NEAREST: 131.64
   - LANCZOS: 131.66
6. Apliquei o filtro GaussianBlur(radius=5).
7. Apliquei o filtro SHARPEN.
8. Salvei as três imagens processadas.

### Conceitos aprendidos
- resize(): altera as dimensões de uma imagem.
- Interpolação: calcula os pixels durante o redimensionamento.
- NEAREST: utiliza o pixel mais próximo.
- LANCZOS: utiliza uma interpolação mais elaborada.
- GaussianBlur: suaviza detalhes e contornos.
- SHARPEN: realça a nitidez aparente.
- save(): grava a imagem processada em um arquivo.

### Resultados
- PAULO_redimensionada.png
- PAULO_desfocada.png
- PAULO_nitida.png

### Conclusão
Aprendi a modificar as dimensões e a aparência de
fotografias com Python, Pillow e NumPy.

Também compreendi que diferentes métodos de
interpolação podem produzir resultados visuais
distintos, mesmo com médias RGB semelhantes.




---

## Laboratório 09 — Preparação de Imagens para IA

### Objetivo
Aprender a preparar fotografias para utilização em
modelos de inteligência artificial e aprendizado de máquina.

### Atividades realizadas
1. Carreguei a fotografia PAULO.jpeg com Pillow.
2. Padronizei suas dimensões para 224 × 224 pixels.
3. Converti a fotografia em uma matriz NumPy.
4. Analisei o formato da matriz: (224, 224, 3).
5. Converti os pixels de uint8 para float32.
6. Normalizei os valores RGB dividindo-os por 255.
7. Comparei a imagem original com a normalizada.
8. Verifiquei que a normalização preservou os valores
   dos pixels ao reconstruir a escala original.
9. Adicionei a dimensão de batch usando np.expand_dims().
10. Obtive uma matriz com formato (1, 224, 224, 3).

### Conceitos aprendidos

- Padronização: adequação das dimensões das imagens.
- RGB: três canais de cores por pixel.
- uint8: números inteiros de 0 a 255.
- float32: números de ponto flutuante de 32 bits.
- Normalização: transformação dos pixels para a escala 0–1.
- Batch: conjunto de imagens organizado em uma matriz.
- NHWC: ordem batch, altura, largura e canais.
- np.expand_dims(): adiciona uma dimensão à matriz.

### Resultados

Dimensões originais: (1021, 1600)
Dimensões padronizadas: (224, 224)
Formato RGB: (224, 224, 3)

Tipo original: uint8
Tipo normalizado: float32

Menor valor normalizado: 0.0
Maior valor normalizado: 0.9843137

Pixel original: [138 115 102]
Pixel normalizado: [0.5411765 0.4509804 0.4]

Maior diferença após reconstrução: 0.0
Diferença média após reconstrução: 0.0

Formato com batch: (1, 224, 224, 3)

### Observações importantes

O redimensionamento direto para 224 × 224 pode
distorcer imagens que não sejam originalmente quadradas.

Nem todos os modelos de IA utilizam a mesma
normalização ou organização dos canais.

### Conclusão

Aprendi a transformar uma fotografia em uma matriz
numérica padronizada, normalizada e organizada em
um lote para utilização em modelos de IA.

Compreendi que preparar os dados é uma etapa
fundamental antes de executar modelos de
aprendizado de máquina.



## Laboratório 10 — Miniprojeto Integrador

### Objetivo
Desenvolver um pipeline de processamento de imagens
reunindo os conhecimentos adquiridos no Capítulo 02.

### Ferramentas utilizadas
- Python
- Pillow
- NumPy
- Matplotlib
- Jupyter Notebook
- VS Code

### Atividades realizadas
1. Carreguei a fotografia PAULO.jpeg.
2. Analisei suas dimensões, canais e tipo de dados.
3. Converti a fotografia RGB para escala de cinza.
4. Redimensionei a imagem preservando a proporção.
5. Apliquei desfoque gaussiano.
6. Apliquei um filtro de nitidez.
7. Preparei uma versão de 224 × 224 pixels para IA.
8. Normalizei os pixels para a escala de 0 a 1.
9. Adicionei uma dimensão de batch.
10. Salvei cinco imagens processadas em arquivos PNG.

### Resultados obtidos

Fotografia original:
- Dimensões: (1021, 1600)
- Matriz: (1600, 1021, 3)
- Tipo: uint8

Escala de cinza:
- Modo: L
- Matriz: (1600, 1021)

Redimensionamento proporcional:
- Dimensões: (255, 400)

Preparação para IA:
- Dimensões: (224, 224)
- Matriz RGB: (224, 224, 3)
- Tipo normalizado: float32
- Batch: (1, 224, 224, 3)
- Menor valor: 0.0
- Maior valor: 0.9843137

### Arquivos gerados

Pasta: imagens/resultados_lab10/

- PAULO_cinza.png
- PAULO_redimensionada.png
- PAULO_desfocada.png
- PAULO_nitida.png
- PAULO_preparada_ia.png

### Aprendizados

Compreendi a diferença entre as dimensões
apresentadas pelo Pillow e pelo NumPy.

Aprendi a converter imagens RGB para escala
de cinza e a redimensionar fotografias sem
distorcer suas proporções.

Pratiquei a aplicação de filtros, a normalização
dos pixels e a organização de imagens em batches.

Também aprendi a organizar e salvar os resultados
de um pipeline de processamento de imagens.

### Conclusão

Concluí o miniprojeto integrador, reunindo
os principais conceitos praticados nos
10 laboratórios de processamento de imagens.

O projeto demonstra as etapas básicas de
preparação e transformação de imagens,
incluindo operações úteis em aplicações de
visão computacional e inteligência artificial.

