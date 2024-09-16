import cv2
import pickle
# Importa a biblioteca OpenCV para manipulação de imagens e vídeos
# Importa a biblioteca pickle para carregar dados serializados

# Inicializa uma lista vazia para armazenar as coordenadas das vagas de estacionamento
vagas = []
# Abre o arquivo 'vagas.pickle' em modo de leitura binária e carrega os dados na lista 'vagas'
with open('Estacionamento\\vagas.pickle', 'rb') as arquivo:
    vagas = pickle.load(arquivo)

# Abre o vídeo 'video.mp4' para processamento
video = cv2.VideoCapture('Estacionamento\\video.mp4')

# Loop para processar cada frame do vídeo
while True:
    # Lê um frame do vídeo
    check, img = video.read()
    # Se não conseguir ler o frame, sai do loop
    if not check:
        break
    # Converte a imagem para escala de cinza
    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aplica um limiar adaptativo para binarizar a imagem
    imgTR = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    # Aplica um filtro de mediana para reduzir ruídos
    imgMedian = cv2.medianBlur(imgTR, 5)
    # Dilata a imagem para preencher pequenas falhas
    imgDil = cv2.dilate(imgMedian, (3,3))

    # Inicializa o contador de vagas em aberto
    vagasEmAberto = 0
    # Itera sobre as coordenadas das vagas de estacionamento
    for x,y,w,h in vagas:    
        # Recorta a região da vaga na imagem dilatada
        vaga = imgDil[y:y+h, x:x+w]
        # Conta os pixels não zero na região da vaga
        count = cv2.countNonZero(vaga)
        # Desenha o número de pixels não zero na imagem original
        cv2.putText(img, str(count), (x,y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        # Se a contagem for maior que 600, considera a vaga ocupada e desenha um retângulo vermelho
        if count > 600:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
        # Caso contrário, considera a vaga livre e desenha um retângulo verde
        else:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
            # Incrementa o contador de vagas em aberto
            vagasEmAberto += 1

        # Desenha um retângulo verde na parte superior da imagem para exibir o contador de vagas em aberto
        cv2.rectangle(img, (90,0), (800, 60), (0, 255, 0), -1)
        # Exibe o contador de vagas em aberto na imagem
        cv2.putText(img, f'Vagas em aberto: {vagasEmAberto}/69', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    # Mostra a imagem processada em uma janela
    cv2.imshow('video', img)
    # Se a tecla 'q' for pressionada, sai do loop
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

