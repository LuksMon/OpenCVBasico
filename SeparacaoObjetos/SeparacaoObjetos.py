import cv2
"""
Exemplo de Mofologia de Fechamento e Detecção de Contornos em OpenCV separando objetos detectados como imagens separadas.


Este script utiliza a biblioteca OpenCV para processar uma imagem, detectar contornos e salvar objetos detectados como imagens separadas.
Linhas do código:
1. Importa a biblioteca OpenCV.
2. Carrega a imagem a partir do caminho especificado.
3. Redimensiona a imagem para 800x600 pixels.
4. Cria uma cópia da imagem original.
5. Converte a imagem para escala de cinza.
6. Aplica o detector de bordas Canny na imagem em escala de cinza com thresholds 100 e 200.
7. Aplica o detector de bordas Canny na imagem em escala de cinza com thresholds 30 e 200 (exemplo do curso).
8. Aplica a operação de fechamento morfológico na imagem resultante do Canny com kernel 5x5.
9. Aplica a operação de fechamento morfológico na imagem resultante do Canny2 com kernel 7x7 (exemplo do curso).
10. Encontra os contornos na imagem após a operação de fechamento.
11. Encontra os contornos na imagem após a operação de fechamento (exemplo do curso).
12-16. Para cada contorno encontrado, desenha um retângulo ao redor do contorno na imagem original.
17. Exibe a imagem original com os retângulos desenhados.
18. Inicializa um contador para nomear os objetos salvos.
19-25. Para cada contorno encontrado na segunda imagem, salva o objeto detectado como uma imagem separada e desenha um retângulo ao redor do contorno.
26. Exibe a segunda imagem com os retângulos desenhados.
29-41. Verifica se a imagem foi carregada corretamente. Se sim, exibe várias versões da imagem processada e espera por uma tecla para fechar as janelas.
"""

# Carregar a imagem
img = cv2.imread('C:\\Fontes\\IA\\ProjetosTeste\\OpenCVBasico\\SeparacaoObjetos\\objetos.jpg')
img = cv2.resize(img, (800, 600))
img2 = img.copy()

imgcinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(imgcinza, 100, 200)
imgCanny2 = cv2.Canny(imgcinza, 30, 200) #Exemplo do curso
imgclose = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, (5, 5))
imgclose2 = cv2.morphologyEx(imgCanny2, cv2.MORPH_CLOSE, (7, 7)) #Exemplo do curso

contours, hierarchy = cv2.findContours(imgclose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2 = cv2.findContours(imgclose2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #Exemplo do curso


for cnt in contours:
    #cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Imagem', img)

num0b = 1
for cnt in contours2:
    #cv2.drawContours(img2, cnt, -1, (0, 0, 255), 2)
    x, y, w, h = cv2.boundingRect(cnt)
    objeto = img2[y:y+h, x:x+w]
    cv2.imwrite(f'C:\\Fontes\\IA\\ProjetosTeste\\OpenCVBasico\\SeparacaoObjetos\\ImgGeradas\\objeto{num0b}.jpg', objeto) 
    cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 2)
    num0b += 1  
cv2.imshow('Imagem 2', img2)


# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro: Não foi possível carregar a imagem.")
else:
    # Mostrar a imagem
    cv2.imshow('Imagem', img)
    cv2.imshow('Imagem Cinza', imgcinza)
    cv2.imshow('Imagem Canny', imgCanny)
    cv2.imshow('Imagem Canny2', imgCanny2)  
    cv2.imshow('Imagem Close', imgclose)
    cv2.imshow('Imagem Close2', imgclose2)
    cv2.imshow('Imagem Contornos', contours)
    cv2.imshow('Imagem Contornos2', contours2)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()