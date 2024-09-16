"""
Este script utiliza a biblioteca OpenCV para selecionar regiões de interesse (ROIs) em uma imagem de um estacionamento e salva essas regiões em um arquivo pickle.
Funções principais:
1. Importa as bibliotecas necessárias: cv2 e pickle.
2. Carrega uma imagem do estacionamento.
3. Inicializa uma lista vazia para armazenar as coordenadas das vagas de estacionamento.
4. Itera 69 vezes para permitir a seleção de 69 vagas de estacionamento:
    - Usa a função cv2.selectROI para selecionar uma ROI na imagem.
    - Fecha a janela de seleção de ROI.
    - Adiciona as coordenadas da ROI à lista de vagas.
    - Desenha um retângulo ao redor de cada ROI na imagem.
5. Salva a lista de coordenadas das vagas em um arquivo pickle.
6. Exibe a imagem com os retângulos desenhados ao redor das vagas até que a tecla 'q' seja pressionada.
Linhas do código:
- `import cv2`: Importa a biblioteca OpenCV.
- `import pickle`: Importa a biblioteca pickle para serialização de objetos.
- `img = cv2.imread('Estacionamento\\Estacionamento.png')`: Carrega a imagem do estacionamento.
- `vagas = []`: Inicializa uma lista vazia para armazenar as coordenadas das vagas.
- `for x in range(69)`: Itera 69 vezes para permitir a seleção de 69 vagas.
- `vaga = cv2.selectROI('vagas', img, False)`: Seleciona uma ROI na imagem.
- `cv2.destroyWindow('vagas')`: Fecha a janela de seleção de ROI.
- `vagas.append((vaga))`: Adiciona as coordenadas da ROI à lista de vagas.
- `for x,y,w,h in vagas`: Itera sobre as coordenadas das vagas.
- `cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)`: Desenha um retângulo ao redor de cada ROI na imagem.
- `with open('Estacionamento\\vagas.pickle', 'wb') as arquivo`: Abre um arquivo pickle para escrita.
- `pickle.dump(vagas, arquivo)`: Salva a lista de coordenadas das vagas no arquivo pickle.
- `while True`: Loop infinito para exibir a imagem.
- `cv2.imshow('Image', img)`: Exibe a imagem com os retângulos desenhados.
- `if cv2.waitKey(1) & 0xFF == ord('q')`: Verifica se a tecla 'q' foi pressionada.
- `break`: Sai do loop se a tecla 'q' for pressionada.
- `cv2.destroyAllWindows()`: Fecha todas as janelas do OpenCV.
"""
import cv2
import pickle

img = cv2.imread('Estacionamento\\Estacionamento.png')

vagas = []

for x in range(69):
    vaga = cv2.selectROI('vagas', img, False)
    cv2.destroyWindow('vagas')
    vagas.append((vaga))  

    for x,y,w,h in vagas:    
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)   


with open('Estacionamento\\vagas.pickle', 'wb') as arquivo:
    pickle.dump(vagas, arquivo)

while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
cv2.destroyAllWindows()
