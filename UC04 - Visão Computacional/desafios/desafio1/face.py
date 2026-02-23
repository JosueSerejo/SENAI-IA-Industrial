# Comando wget para baixar a imagem (necessário para rodar no Colab)
!wget -O dw2.jpeg "https://i.imgur.com/q7FlMii.jpeg"

import cv2
# Importação para exibir gráfico
import matplotlib.pyplot as plt 

# Carregar o classificador Haar Cascade para detecção de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Ler a imagem do disco
image = cv2.imread('dw2.jpeg')

# Verificar as dimensões da imagem
height, width, channels = image.shape
print(f"Dimensões da imagem: {height}x{width}, Canais: {channels}")

# --- [CONCLUSÃO 1: Carregamento e Análise] ---
# A imagem foi carregada com sucesso e verificamos suas dimensões (height/width).
# Essa verificação é importante para saber se a resolução é adequada para o processamento
# e confirmar que a imagem possui 3 canais de cor.

# Converter a imagem de BGR para RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# --- [CONCLUSÃO 2: Conversão de Cores] ---
# O OpenCV carrega imagens no padrão BGR (Blue-Green-Red).
# A conversão foi realizada para manipular a imagem no espaço de cor correto,
# garantindo que as cores não fiquem invertidas durante o processamento ou exibição.

# Detectar rostos na imagem
faces = face_cascade.detectMultiScale(image_rgb, scaleFactor=1.2, minNeighbors=4, minSize=(30, 30))

# --- [CONCLUSÃO 3: Detecção de Objetos] ---
# O método detectMultiScale foi aplicado.
# - scaleFactor=1.2: Reduz a imagem em 20% a cada escala para buscar rostos de tamanhos diferentes.
# - minNeighbors=4: Define quantos vizinhos cada retângulo candidato deve ter para ser mantido,
#   o que ajuda a filtrar falsos positivos e garantir que apenas rostos reais sejam detectados.

# Desenhar retângulos ao redor dos rostos detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)

# --- [CONCLUSÃO 4: Visualização Final] ---
# Os retângulos (bounding boxes) foram desenhados nas coordenadas retornadas pelo classificador.
# Isso valida visualmente que o algoritmo conseguiu localizar a região de interesse (ROI) na imagem.

# Exibir a imagem com os rostos detectados
# Substituído cv2.imshow por plt.imshow conforme solicitado no feedback
plt.imshow(image_rgb)
plt.title('Rostos Detectados')
plt.show()

